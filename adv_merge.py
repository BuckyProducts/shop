# Merge ES+EN day PDFs (from adv_render.js), JPEG-compress raster images (alpha kept). Text stays selectable.
import pikepdf,io
from PIL import Image
def jpegify(pdf):
  for obj in pdf.objects:
    if isinstance(obj,pikepdf.Stream) and obj.get("/Subtype")=="/Image" and obj.get("/Filter")!="/DCTDecode":
      try:
        pim=pikepdf.PdfImage(obj)
        if pim.bits_per_component!=8 or pim.width*pim.height<20000 or str(pim.colorspace) in ("/DeviceGray",):continue
        im=pim.as_pil_image().convert("RGB");b=io.BytesIO();im.save(b,"JPEG",quality=82,optimize=True)
        obj.write(b.getvalue(),filter=pikepdf.Name.DCTDecode);obj.ColorSpace=pikepdf.Name.DeviceRGB
        if "/DecodeParms" in obj:del obj["/DecodeParms"]
        sm=obj.get("/SMask")
        if sm is not None and sm.get("/Filter")!="/DCTDecode":
          a=pikepdf.PdfImage(sm).as_pil_image().convert("L");b2=io.BytesIO();a.save(b2,"JPEG",quality=92);sm.write(b2.getvalue(),filter=pikepdf.Name.DCTDecode)
          if "/DecodeParms" in sm:del sm["/DecodeParms"]
      except Exception as e:pass
import hashlib
def dedupe(pdf):
  canon={}
  def key(o):
    h=hashlib.md5(o.read_raw_bytes());sm=o.get("/SMask")
    if sm is not None:h.update(sm.read_raw_bytes())
    return h.hexdigest()+str(o.get("/Width"))+str(o.get("/Height"))
  def walk(res,seen):
    if res is None or "/XObject" not in res:return
    xo=res.XObject
    for k in list(xo.keys()):
      o=xo[k]
      if o.get("/Subtype")=="/Image":
        kk=key(o)
        if kk in canon:xo[k]=canon[kk]
        else:canon[kk]=o
      elif o.get("/Subtype")=="/Form" and o.objgen not in seen:
        seen.add(o.objgen);walk(o.get("/Resources"),seen)
  for pg in pdf.pages:walk(pg.get("/Resources"),set())
for d in range(1,25):
  out=pikepdf.new()
  for l in("es","en"):
    src=pikepdf.open(f"/workspace/tmp/adv/{l}_{d:02d}.pdf");out.pages.extend(src.pages)
  dedupe(out);out.remove_unreferenced_resources();jpegify(out);out.docinfo["/Title"]=f"Calendario de Adviento Bucky - Dia {d} / Bucky Advent Calendar - Day {d}";out.docinfo["/Author"]="Bucky Little Shop"
  out.save(f"adviento/Bucky-Adviento-Dia-{d:02d}_ES-EN.pdf",compress_streams=True,object_stream_mode=pikepdf.ObjectStreamMode.generate,recompress_flate=True)
print("ok")
