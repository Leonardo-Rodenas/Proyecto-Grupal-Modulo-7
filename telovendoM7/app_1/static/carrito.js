a = JSON.parse(localStorage.getItem('molestia'))
window.addEventListener('load', function () {
    if(a==false){
    window.location.href='anexos/login.html';
}else{
    setTimeout(logout,20000);
    function logout(){
    a=false;
    localStorage.setItem('molestia', JSON.stringify(a));
    window.location.href='anexos/login.html';
}
}})




//lista de articulos del carrito
window.carro = [];

//elimina un articulo del carrito
window.descartarCarro = function () {
    let click = this;
    let eli= click.eli;
    window.carro.splice(eli, 1);
    window.cargarCarro();
};

//crea el articulo para añadirlo al carrito
window.crearArticulo=function(i){
    let cantidad = document.querySelector("#cantidad"+i).value;
    let nombre=producto[i].nombre;
    let precio=producto[i].precio;
    let total=producto[i].precio*cantidad;

    for (let e = 0; e < window.carro.length; e++) {
        let comparador=window.carro[e];
        if (nombre==comparador.nombre){
            eli=e;
            window.descartarCarro()
        }
        
    }
    let articulo={};
    let dato=producto[i].nombre+" x"+cantidad+" $"+producto[i].precio*cantidad;
    
    articulo.dato=dato;
    articulo.precio=precio;
    articulo.nombre=nombre;
    articulo.cantidad=cantidad;
    articulo.total=total;
    window.carro.push(articulo);
    localStorage.setItem('carro', JSON.stringify(carro));
window.cargarCarro();
};

//añade el articulo al carrito
window.cargarCarro = function () {
   
    let llenar = document.querySelector("#carro");
    llenar.innerText="";
    
    for (let i = 0; i < window.carro.length; i++) {
        
    let articuloactual=window.carro[i];

    let tr = document.createElement("tr");
    tr.setAttribute("style","margin-bottom:2px")
    let td = document.createElement("td");
    let botonEliminar = document.createElement('button');
    botonEliminar.classList.add("btn", "btn-danger");
    botonEliminar.innerText = "Descartar";
    botonEliminar.eli = i;
    botonEliminar.addEventListener('click', window.descartarCarro);
    llenar.appendChild(tr);
    tr.appendChild(td);
    td.innerText=articuloactual.dato;
    tr.appendChild(botonEliminar);

    }
    
    let summary = document.querySelector("#divi");
    summary.innerText="";
    let span = document.createElement("span");
    span.classList.add("position-absolute","top-100","start-100","translate-middle","badge","rounded-pill","bg-danger")
    span.setAttribute("id","badge")
    summary.appendChild(span);
    let largo=window.carro.length;
    console.log(window.carro.length);
    let badge = document.querySelector("#badge");
    badge.innerText=largo;
    if(largo==0){
        let badge = document.querySelector("#badge");
    badge.innerText="";
    let tr = document.createElement("tr");
    tr.setAttribute("style","margin-bottom:2px")
    let td = document.createElement("td");
    llenar.appendChild(tr);
    tr.appendChild(td);
    td.innerHTML="";
    td.innerHTML="<h5>Por ahora el carrito está vacio :c</5>";
    }else{
        let botonPagar= document.createElement('a');
    botonPagar.classList.add("btn", "btn-success");
    botonPagar.setAttribute("type","button");
    botonPagar.setAttribute("href","anexos/formulario.html");
    botonPagar.innerText = "Pagar";
    
    llenar.appendChild(botonPagar);

    }
    
}

//evento que se activa al cargarse la pagina
window.addEventListener('load', function () {
    window.cargarPag();
    
})

//crea los elementos de la pagina y los rellena con los productos
window.cargarPag = function () {
    let post = document.querySelector("#inicio>div");
    for (let i = 0; i < window.producto.length; i++) {
        articulo = producto[i];
        let row = document.createElement('div');
        row.classList.add("row", "border", "border-1");
        let col = document.createElement('div');
        col.setAttribute("style", "margin-bottom:20px");
        col.classList.add("col-lg-3", "border", "border-1", "col-sm-12");
        let row2 = document.createElement('div');
        row2.classList.add("row");
        let a = document.createElement('a');
        a.classList.add("row");
        a.setAttribute("href", "productos/" + (i + 1) + ".html");
        let col2 = document.createElement('div');
        col2.classList.add("col-lg-10");
        let img = document.createElement('img');
        img.setAttribute("src", "img/" + (i + 1) + ".jpg");
        img.setAttribute("alt", "");
        img.setAttribute("height", "140");
        let col3 = document.createElement('div');
        col3.classList.add("col-lg-3");
        col3.innerText = articulo.id;
        let col4 = document.createElement('div');
        col4.classList.add("col-lg-4");
        col4.innerText = articulo.nombre;
        let col5 = document.createElement('div');
        col5.classList.add("col-10");
        col5.innerText = articulo.descripcion;
        let col6 = document.createElement('div');
        col6.classList.add("col-5");
        col6.innerText = "$" + articulo.precio;
        let col7 = document.createElement('div');
        col7.classList.add("col-3", "col-lg-6");
        col7.innerText = "Cantidad:";
        let quantity=document.createElement('div');
        quantity.classList.add("quantity");
        let span1 = document.createElement('span');
        span1.classList.add("quantity-add","quantity-button");
        let input = document.createElement('input');
        input.classList.add("quantity-field", "border-0", "text-center");
        input.setAttribute("type", "number");
        input.setAttribute("step", "1");
        input.setAttribute("min", "1");
        input.setAttribute("max", "20");
        input.setAttribute("value", "1");
        input.setAttribute("id", "cantidad" + i);
        let span2 = document.createElement('span');
        span2.classList.add("quantity-remove","quantity-button");
        let col8 = document.createElement('div');
        col8.classList.add("col-3", "col-lg-12");
        let button = document.createElement('button');
        button.classList.add("btn", "btn-light");
        button.innerText = "Añadir al carrito";
        button.setAttribute("onclick", "crearArticulo("+i+")");

        post.appendChild(col);
        col.appendChild(row2);
        row2.appendChild(a);
        a.appendChild(col2);
        col2.appendChild(img);
        a.appendChild(col3);
        a.appendChild(col4);
        row2.appendChild(col5);
        row2.appendChild(col6);
        row2.appendChild(col7);
        col7.appendChild(quantity);
        quantity.appendChild(span1)
        quantity.appendChild(input)
        quantity.appendChild(span2)
        row2.appendChild(col8);
        col8.appendChild(button);

        
    }
    $('.quantity-button').off('click').on('click', function () {
  
        if ($(this).hasClass('quantity-add')) {
          var addValue = parseInt($(this).parent().find('input').val()) + 1;
              $(this).parent().find('input').val(addValue).trigger('change');
          }
      
          if ($(this).hasClass('quantity-remove')) {
          var removeValue = parseInt($(this).parent().find('input').val()) - 1;
              if( removeValue == 0 ) {
            removeValue = 1;
              }
              $(this).parent().find('input').val(removeValue).trigger('change');
          }
      
      });
      
    
}
//base de datos improvisada
window.producto = [{
    "id": "A1",
    "nombre": "Licuadora",
    "descripcion": "LICUADORA SINDELEN L-1500NG Batidos, jugos de frutas y mucho más es lo que puedes preparar con nuestra licuadora PowerMix L-1500NG. Con capacidad de 1,5 lt, tiene 2 velocidades y una resistente jarra de plástico.",
    "precio": '39990'
},
{
    "id": "A2",
    "nombre": "Refrigerador",
    "descripcion": "Refrigerador Top Freezer con motor Smart Inverter Compressor y capacidad total de 254 Litros",
    "precio": "259990",
},
{
    "id": "A3",
    "nombre": "Microondas",
    "descripcion": "Simplifica la preparación de tus recetas favoritas con el Microondas 20L Manual Negro Mademsa (MM20FBM). Su panel ofrece la comodidad que tu rutina en la cocina merece, ya que cuenta con modos de preparación preprogramados en su panel de dos mandos mecánicos, súper fácil de ajustar.",
    "precio": "59990",
},
{
    "id": "A4",
    "nombre": "Cocina",
    "descripcion": "Cocina Gas Midea 4 Quemadores MCG-4QI24NS",
    "precio": "189990",
},
{
    "id": "A5",
    "nombre": "Aire Acondicionado",
    "descripcion": "ON-OFF .CLIMATIZA 25 M2 BAJO RUIDO. MODO TURBO. FUNCIÓN AUTO RESTART. DESHIELO AUTOMÁTICO. TIMER 24 HORAS. FILTRO DE ALTA DENSIDAD. CONTROL WI FI (VENTA POR SEPARADO).",
    "precio": "250000",
},
{
    "id": "A6",
    "nombre": "Ventilador",
    "descripcion": "Ambiente fresco y confortable. El ventilador Midea crea rápidamente un clima de frescura gracias a sus 3 niveles de potencia y cabezal oscilante. Su innovador motor de cobre garantiza un óptimo rendimiento y una gran durabilidad. Calidad y alta funcionalidad para lograr bienestar en todos los espacios.",
    "precio": "69990",
},
{
    "id": "A7",
    "nombre": "Aspiradora",
    "descripcion": "ASPIRADORA COMPACTA, 1600W DE POTENCIA, POTENCIA DE SUCCIÓN 280W, CAPACIDAD 1.5 LT. NO NECESITA BOLSA, SISTEMA CICLÓN ELÍPTICO.",
    "precio": "49990",
},
{
    "id": "A8",
    "nombre": "Califont",
    "descripcion": "Essential 8 Eco GL Sistema de seguridad Sus múltiples sistemas de seguridad garantizan el buen funcionamiento de su calefón y su bienestar. Ecológico Utiliza un intercambiador de calor de cobre libre de oxígeno, lo que lo hace más amigable con el medio ambiente. Eficiente La avanzada tecnología de sus quemadores e intercambiador de calor, resultan en un calentamiento de agua más eficiente. Encendido electrónico Con solo abrir la llave de agua caliente.",
    "precio": "119990",
},
{
    "id": "A9",
    "nombre": "Lavadora",
    "descripcion": "Lavadora de Carga Superior con motor Smart Inverter y capacidad total de 19 kilos WT19BSB. Este modelo cuenta con características principales como un diseño sofisticado y tecnología de primera como la de su motor Smart Inverter con 10 años de garantía. Gracias al motor Smart Inverter el tambor logra tener un funcionamiento con 3 tipos de movimientos, que logra brindar un mejor desempeño de lavado y resultados de lavado en las prendas.",
    "precio": "358990",
},
{
    "id": "A10",
    "nombre": "Centrifuga",
    "descripcion": "Lavadora centrífuga semiautomática carga superior modelo LC-4550 de Sindelen. Cuenta con una capacidad de lavado de 4.2 Kg. ropa seca y una capacidad de centrifugado de 3.2 Kg. Es bajo ruido y posee un sistema Reversomatic que reduce el enredo de la ropa mientras se lava.",
    "precio": "119990",

}]
