$(document).ready(()=>{
    console.log("log")
    var view = $("#view")
    view.load(
        "/images/IMG_2020011811_3010_0791.jpg",
        (data)=>{
            console.log(data)
        }
    )
})