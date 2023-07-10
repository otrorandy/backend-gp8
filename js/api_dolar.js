const apiUrl= "https://www.dolarsi.com/api/api.php?type=valoresprincipales"

async function obtenerPrecioEnPesos(){
    try{
        const response = await fetch(apiUrl);
        const data = await response.json();
        const dolarBlue = await parseInt(data[1].casa.venta);
        var precioEnPesos = (dolarBlue*500).toLocaleString();
        document.getElementById("precio_pesos").innerHTML = precioEnPesos;
    }
    catch(error) {console.log('Ocurrio un error grave', error)}
}
obtenerPrecioEnPesos()