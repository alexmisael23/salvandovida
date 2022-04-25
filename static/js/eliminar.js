$(document).ready(function()
{
    $('.dltBtn').click(function(e){
    e.preventDefault();
    var id = $(this).attr('data-id');
    var parent = $(this).parent("td").parent("tr");
    bootbox.dialog(
        {
            message: "¿Estás seguro de eliminar el registro?",
            title: "<i class='fa fa-trash-o'></i> ¡Atención!",
            buttons: {
                cancel: {
                    label: "No",
                    className: "btn-success",
                    callback: function() {
                    $('.bootbox').modal('hide');
                                         }
                        },
                confirm: {
                    label: "Eliminar",
                    className: "btn-danger",
                    callback: function() {
                    $.ajax({
                    url: '/eliminar_persona',
                    data: {id:id}
                            })
                //Si todo ha ido bien...
                .done(function(response){
                parent.fadeOut('slow'); //Borra la fila afectada
                })
                .fail(function(){
                    bootbox.alert('Algo ha ido mal. No se ha podido completar la acción.');
                    })
                                        }
                            }
                }
            });
            });
            });