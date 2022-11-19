function show_dist(ssid){
    console.log(ssid)
    var router ={
        "ssid":ssid
    }
    fetch("/calculDist",{
        method:"POST",
        credentials:"include",
        body:JSON.stringify(router),
        cache:"no-cache",
        headers: new Headers({
            "content-type": "application/json"
        })

    })
        .then((r)=> r.json())
        .then((json) => {
            const d = document.querySelector("#calculated-distance");
            d.innerHTML=json['distance']+" Metre"
        })
}
















/*{let routers = document.getElementsByClassName(".list-routers-item");
let selectedRouter = routers[0] || null;
console.log(routers)
routers.forEach((r)=>{
    r.addEventListener('click', handleClick);
})

function distance(){
    selectedRouter=this.innerHTML;
}

const calculateDistance = async function (){
    let distance = 0;
    console.log("disttest")
    const res = await fetch("/calculDist/?routerid="+selectedRouter)
        .then(res => res.data)
        .then(res => {
            //mathalan
            distance = res.distance;
            let distElt = document.getElementById("calculated-distance");
            distElt.innerHTML = distance;
        })
        .catch((e) => console.log(e));
}*/
