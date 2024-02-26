import markdown2
from pyscript import document

def convert(i):
    output_div = document.querySelector("#render")
    output_code = document.querySelector("#code")
    input_box = document.querySelector("#mark")
    content = ""
    for i in str(markdown2.markdown(input_box.value)).splitlines():
        if i != "":
            content = content + i + "\n"
    output_div.innerHTML = content
    output_code.value = content

convert(None)
