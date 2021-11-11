#Eiud Roberto Rangel Camacho
Write-Host "Bienvenido"
while($true){
    $opc = Read-Host -Prompt "¿Que servicio desea realizar? [1]Ver Status [2]Cambiar Status [3]Ver Red Actual 
    [4]Cambiar Red Actual [5]Ver Reglas De Bloqueo [6]Agregar Reglas De Bloqueo [7]Eliminar Reglas De Bloqueo [8]Salir"

    Switch($opc){
        1{
            Ver-StatusPerfil
        }
        2{
            Cambiar-StatusPerfil
        }
        3{
            Ver-PerfilRedActual
        }
        4{
            Cambiar-PerfilRedActual
        }
        5{
            Ver-ReglasBloqueo
        }
        6{
            Agregar-ReglasBloqueo
        }
        7{
            Eliminar-ReglasBloqueo
        }
        8{
           exit
        }
        default{
            Write-Host "Ingrese un valor Valido"
        }
    }
}