function updateGraph(){
    fetch("/graph")
        .then((r)=> r.json())
        .then((json) => {
            const img = document.querySelector("#graph-img");
            const parent = img.parentNode;

            let newimg = document.createElement("img");
            parent.removeChild(img);
            newimg.src = "data:image/png;base64, "+json['img']
            parent.appendChild(newimg)
        })
}