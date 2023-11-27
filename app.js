function runPyScript(input){
    var jqXHR = $.ajax({
        type: "POST",
        url: "/login",
        async: false,
        data: { mydata: input }
    });

    return jqXHR.responseText;
}

