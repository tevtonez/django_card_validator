$("#button").click(function () {
  var card_number = $("#id_card_number").val();
  $("#result").removeClass();

  $.ajax({
    type: "POST",
    url: "api/check_number/",
    data: {
      'card_number': card_number
    },
    dataType: 'json',
    success: function (data) {
      if (data.result) {
          $("#result").html(data.result).addClass("alert alert-" + data.result_class);
      }
    }
  });
});

$("#validator").submit(function(){
    var card_number = $("#id_card_number").val();
  $("#result").removeClass();

  $.ajax({
    type: "POST",
    url: "api/check_number/",
    data: {
      'card_number': card_number
    },
    dataType: 'json',
    success: function (data) {
      if (data.result) {
          $("#result").html(data.result).addClass("alert alert-" + data.result_class);
      }
    }
  });
})
