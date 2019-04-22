( function( ) {
    const txtName = document.getElementById( "txtName" );
    const nameForm = document.getElementById( "nameForm" );
    const datalist = document.getElementById("datalist-event");
    const titleEvennt = document.getElementById("event-now");
    var count = 0;
    const FLAG_DETECTED = -2;

    txtName.focus();
    titleEvennt.innerHTML = datalist.value;
    txtName.addEventListener("input",  ( e ) => {
        count++;
        
        if( e.data === "'" ) {
            console.log( txtName.value)
            txtName.value = txtName.value.replace( "'", "-");
      
            count = FLAG_DETECTED;
        }else if (e.data === '-'){
           
            count = FLAG_DETECTED;



        }
       
        if( count === ( FLAG_DETECTED + 1 ) ) {
        console.log( txtName.value)
            var timer = function(){
                submit( txtName.value ); 
            };
    
               setTimeout(timer,1000);
          
           
           
        }
    } );






 
    nameForm.addEventListener("submit", ( e ) => {
        e.preventDefault();
        submit( txtName.value );
    } );

    function submit( text) {
        if( validateRut( text ) ) {
         /*    txtResults.innerHTML += text + "<br/>"; */
            txtName.value = "";
            count = 0;
            return true
        } else {
            alert( "rut ingresado no es válido" );
            txtName.value = "";
        }
    }

    // POR FAVOR VALIDAR EL RUT CORRECTAMENRTE PARA QUE ENTRE EN LA APLICACION
    function validateRut( rut ) {
        nameForm.submit();
        return true;
    }
}) ( );

function soloRut(string){//Solo ruts formato con guión
    var out = '';
    var filtro = '1234567890k-K';//Caracteres validos
	
    //Recorrer el texto y verificar si el caracter se encuentra en la lista de validos 
    for (var i=0; i<string.length; i++)
       if (filtro.indexOf(string.charAt(i)) != -1) 
             //Se añaden a la salida los caracteres validos
	     out += string.charAt(i);
	 
    //Retornar valor filtrado
    return out;
} 



