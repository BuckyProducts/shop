# Build 24 text-based, small bilingual Advent PDFs from the Christmas bundle pages (ES+EN). Images -> JPEG (alpha kept as SMask).
from pypdf import PdfReader,PdfWriter
from pypdf.generic import NameObject
from PIL import Image
import io
E="/workspace/buckyproducts/etsy/bundle1/pdf/";en=PdfReader(E+"Christmas-Party-Printables_EN_US-Letter.pdf");es=PdfReader(E+"Kit-Posada-e-Intercambio_ES_US-Letter.pdf")
P=[3,4,5,6,7,18,19,20,22,23,24,25,57,61,62,64,66,68,69,70,71,72,73,75]
def shrink(w):
  seen=set()
  for pg in w.pages:
    xo=pg["/Resources"].get("/XObject")
    if not xo:continue
    for k in xo:
      o=xo[k].get_object()
      if o.get("/Subtype")!="/Image" or id(o) in seen or o.get("/Filter")=="/DCTDecode":continue
      seen.add(id(o))
      try:
        from pypdf.filters import _xobj_to_image
        ext,img,_=_xobj_to_image(o)[:3] if False else (None,None,None)
      except Exception:pass
      # decode raw RGB
      W,H=int(o["/Width"]),int(o["/Height"]);cs=o.get("/ColorSpace");data=o.get_data()
      if cs!="/DeviceRGB" or int(o.get("/BitsPerComponent",8))!=8 or len(data)!=W*H*3:continue
      im=Image.frombytes("RGB",(W,H),data);b=io.BytesIO();im.save(b,"JPEG",quality=82,optimize=True)
      o.set_data(b.getvalue()) if False else None
      o._data=b.getvalue();o[NameObject("/Filter")]=NameObject("/DCTDecode")
      if "/DecodeParms" in o:del o["/DecodeParms"]
for d,p in enumerate(P,1):
  w=PdfWriter();w.add_page(es.pages[p-1]);w.add_page(en.pages[p-1]);shrink(w)
  w.compress_identical_objects(remove_identicals=True,remove_orphans=True)
  w.add_metadata({"/Title":f"Calendario de Adviento Bucky - Día {d} / Bucky Advent Calendar - Day {d}","/Author":"Bucky Little Shop"})
  w.write(f"adviento/Bucky-Adviento-Dia-{d:02d}_ES-EN.pdf")
print("ok")
