// $(function () {
//     $("#tabs").tabs();
// });

function tbodyData(data) {
    var dis_tbData;
    Object.keys(data['disease']).forEach(function (key) {
        dis_tbData += `<tr>`;
        data['disease'][key].forEach(function (val) {
            dis_tbData += `<td>${val}</td>`;
        })
        dis_tbData += `<tr>`
    });
    $('#diseaseTable').find('tbody').append(dis_tbData);

    var disVar_tbData;
    Object.keys(data['variant']).forEach(function (key) {
        disVar_tbData += `<tr>`;
        data['variant'][key].forEach(function (val) {
            if (val != null) {
                let newVal = val.replace(/_/g, " ");
                disVar_tbData += `<td>${newVal}</td>`;
            } else {
                disVar_tbData += `<td>N/A</td>`;
            }
        })
        disVar_tbData += `<tr>`
    });
    if (data['variant'].length >= 12) {
        $('#disVarianTable').css({
            width: '1099px',
            overflow: 'scroll',
            height: '700px'
        });
    }
    $('#disVarianTable').find('tbody').append(disVar_tbData);
}

// http://localhost/rare_db/result.html?disease=Achondroplasia

let searchParams = new URLSearchParams(window.location.search)
if(searchParams.has('disease') === true){
    let param = searchParams.get('disease')
    $.ajax({                                    // SQL Query using ajax
        url: './cgi/getData.cgi',
        data:{
            'sel_Query': 'disease',
            'queryTerm': param
        },
        dataType: 'json',
        success: function (data) {
            tbodyData(data);
        }
    });
}else if(searchParams.has('gene') === true){
    let param = searchParams.get('gene')
    $.ajax({                                    // SQL Query using ajax
        url: './cgi/getData.cgi',
        data:{
            'sel_Query': 'gene',
            'queryTerm': param
        },
        dataType: 'json',
        success: function (data) {
            tbodyData(data);
        }
    });
}else{
    let param = searchParams.get('variant')
    $.ajax({                                    // SQL Query using ajax
        url: './cgi/getData.cgi',
        data:{
            'sel_Query': 'variant',
            'queryTerm': param
        },
        dataType: 'json',
        success: function (data) {
            tbodyData(data);
        }
    });
}