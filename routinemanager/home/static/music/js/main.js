$('.apireq').click( function() {
    $.ajax({
             url : "http://localhost:8000/programs",
             dataType: "json",
             success : function (data) {
                      $('#departmentid').text( data[0].departmentid);
                      $('#programid').text( data[0].programid);
                      $('#programname').text( data[0].programname);

                    }
                 });
             });