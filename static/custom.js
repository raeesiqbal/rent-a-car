var $ = jQuery.noConflict();

//Car Appear In View
function isScrolledIntoView(elem) {
  var docViewTop = $(window).scrollTop();
  var docViewBottom = docViewTop + $(window).height();

  var elemTop = $(elem).offset().top + 180;
  var elemBottom = elemTop + $(elem).height() - 500;

  return elemBottom <= docViewBottom && elemTop >= docViewTop;
}

$(window).scroll(function () {
  $(".running-car").each(function () {
    if (isScrolledIntoView(this) === true) {
      $(this).addClass("in-view");
    } else {
      $(this).removeClass("in-view");
    }
  });
});
jQuery(".bt-switch").bootstrapSwitch();

$("[name='type']").change(function () {
  if ($(".yes").is(":checked") != true) {
    $("#to").hide();
    $("#from").hide();
    $("#city").show();
  } else {
    $("#to").show();
    $("#from").show();
    $("#city").hide();
  }
});

$("[name='from']").change(function () {
  var vl = $("[name='from']").val();
  $(`[name='to'] option[value=${vl}]`)
    .attr("disabled", "disabled")
    .siblings()
    .removeAttr("disabled");
});

$("[name='to']").change(function () {
  var vl = $("[name='to']").val();
  $(`[name='from'] option[value=${vl}]`)
    .attr("disabled", "disabled")
    .siblings()
    .removeAttr("disabled");
});

function bookCar(id) {
  var type = $('input[name="type"]:checked').val();
  var from = $("[name='from']").val();
  var to = $("[name='to']").val();
  var city = $("[name='city']").val();
  $("#booking_type").val(type);
  $("#booking_price_id").val(id);
  $.ajax({
    type: "get",
    url: `/city/${id}/${type}`,
    dataType: "json",
    success: function (data) {
      $("#city-image").attr(
        "style",
        `background-image:url(${data["data"]["image"]}); background-size:cover`
      );
      if (type == "Yes") {
        $("#title").html(`
                Book Car from ${from} to ${to} 
            `);
      } else {
        $("#title").html(`
                Book Car - ${city} 
            `);
      }
    },
    error: (err) => {
      // console.log(err);
    },
    cache: false,
    contentType: false,
    processData: false,
  });
}

function getCookie(name) {
  let cookieValue = null;
  if (document.cookie && document.cookie !== "") {
    const cookies = document.cookie.split(";");
    for (let i = 0; i < cookies.length; i++) {
      const cookie = cookies[i].trim();
      // Does this cookie string begin with the name we want?
      if (cookie.substring(0, name.length + 1) === name + "=") {
        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
        break;
      }
    }
  }
  return cookieValue;
}
$("#booking-form").on("submit", function (e) {
  e.preventDefault();
  var form = $(this);
  var formData = new FormData(this);
  var url = form.attr("action");

  $.ajax({
    type: "POST",
    url: url,
    data: formData,
    headers: {
      "X-Requested-With": "XMLHttpRequest",
      "X-CSRFToken": getCookie("csrftoken"),
    },
    success: function (data) {
      setTimeout(function () {
        $(".mfp-close").click();
      }, 1000);

      const toastLiveExample = document.getElementById("liveToast");
      const toast = new bootstrap.Toast(toastLiveExample);
      toast.show();
    },
    error: (err) => {},
    cache: false,
    contentType: false,
    processData: false,
  });
});

$(window).on("load", function () {
  var vl_to = $("[name='to']").val();
  var vl_from = $("[name='from']").val();
  $(`[name='from'] option[value=${vl_to}]`)
    .attr("disabled", "disabled")
    .siblings()
    .removeAttr("disabled");
  $(`[name='to'] option[value=${vl_from}]`)
    .attr("disabled", "disabled")
    .siblings()
    .removeAttr("disabled");
});

$(function () {
  $(".component-datepicker.default").datepicker({
    autoclose: true,
    startDate: "today",
  });

  $(".component-datepicker.today").datepicker({
    autoclose: true,
    startDate: "today",
    todayHighlight: true,
  });

  $(".component-datepicker.past-enabled").datepicker({
    autoclose: true,
  });

  $(".component-datepicker.format").datepicker({
    autoclose: true,
    format: "dd-mm-yyyy",
  });

  $(".component-datepicker.autoclose").datepicker();

  $(".component-datepicker.disabled-week").datepicker({
    autoclose: true,
    daysOfWeekDisabled: "0",
  });

  $(".component-datepicker.highlighted-week").datepicker({
    autoclose: true,
    daysOfWeekHighlighted: "0",
  });

  $(".component-datepicker.mnth").datepicker({
    autoclose: true,
    minViewMode: 1,
    format: "mm/yy",
  });

  $(".component-datepicker.multidate").datepicker({
    multidate: true,
    multidateSeparator: " , ",
  });

  $(".component-datepicker.input-daterange").datepicker({
    autoclose: true,
  });

  $(".component-datepicker.inline-calendar").datepicker();

  $(".datetimepicker").datetimepicker({
    showClose: true,
  });

  $(".datetimepicker1").datetimepicker({
    format: "LT",
    showClose: true,
  });

  $(".datetimepicker2").datetimepicker({
    inline: true,
    sideBySide: true,
  });

  $(".datetimepicker3,.datetimepicker4").datetimepicker();

  // .daterange1
  $(".daterange1").daterangepicker({
    buttonClasses: "button button-rounded button-mini m-0",
    applyClass: "button-color",
    cancelClass: "button-light",
  });

  // .daterange2
  $(".daterange2").daterangepicker({
    opens: "center",
    timePicker: true,
    timePickerIncrement: 30,
    locale: {
      format: "MM/DD/YYYY h:mm A",
    },
    buttonClasses: "button button-rounded button-mini m-0",
    applyClass: "button-color",
    cancelClass: "button-light",
  });

  // .daterange3
  $(".daterange3").daterangepicker(
    {
      singleDatePicker: true,
      showDropdowns: true,
    },
    function (start, end, label) {
      var years = moment().diff(start, "years");
      alert("You are " + years + " years old.");
    }
  );

  // reportrange
  function cb(start, end) {
    $(".reportrange span").html(
      start.format("MMMM D, YYYY") + " - " + end.format("MMMM D, YYYY")
    );
  }
  cb(moment().subtract(29, "days"), moment());

  $(".reportrange").daterangepicker(
    {
      buttonClasses: "button button-rounded button-mini m-0",
      applyClass: "button-color",
      cancelClass: "button-light",
      ranges: {
        Today: [moment(), moment()],
        Yesterday: [moment().subtract(1, "days"), moment().subtract(1, "days")],
        "Last 7 Days": [moment().subtract(6, "days"), moment()],
        "Last 30 Days": [moment().subtract(29, "days"), moment()],
        "This Month": [moment().startOf("month"), moment().endOf("month")],
        "Last Month": [
          moment().subtract(1, "month").startOf("month"),
          moment().subtract(1, "month").endOf("month"),
        ],
      },
    },
    cb
  );

  // .daterange4
  $(".daterange4").daterangepicker({
    autoUpdateInput: false,
    locale: {
      cancelLabel: "Clear",
    },
    buttonClasses: "button button-rounded button-mini m-0",
    applyClass: "button-color",
    cancelClass: "button-light",
  });

  $(".daterange4").on("apply.daterangepicker", function (ev, picker) {
    $(this).val(
      picker.startDate.format("MM/DD/YYYY") +
        " - " +
        picker.endDate.format("MM/DD/YYYY")
    );
  });

  $(".daterange4").on("cancel.daterangepicker", function (ev, picker) {
    $(this).val("");
  });
});
