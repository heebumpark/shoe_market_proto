function Geo_confirm(position){
    const lat = position.coords.latitude;
    const long = position.coords.longitude;
    console.log("사용자의 위치", lat, long);
}
function Geo_error(){
    alert("사용자 위치를 찾을 수가 없다 냥");
}

navigator.geolocation.getCurrentPosition(Geo_confirm, Geo_error)