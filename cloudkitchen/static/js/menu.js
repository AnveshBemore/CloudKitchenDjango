var count = 0;
setCount();
function setCount() {
  var cou = localStorage.getItem("count");
  document.getElementById("countorders").innerHTML = cou;
  var x = document.getElementById("sign").innerHTML;
  if (x !== "signin") {
    // console.log("xxxxxxxxxxxxxxxxxxxxx");
    localStorage.setItem("uname", x);
  }
  var unam = localStorage.getItem("uname");
  document.getElementById("sign").innerHTML = unam;
  console.log(x + " xxxxxxxxxxxxxxxxxxxxxxx");
}
function plus(x) {
  //   var ele = document.getElementById("countorders");
  //   count = Number(ele.innerHTML);
  count = Number($("#countorders").html());
  count++;
  localStorage.setItem("count", count);
  console.log(localStorage);
  console.log(count);
  // alert(count);
  $("#countorders").html(count);
  // alert(this.attr("id"));
  // alert(this.)
  // addp(this, this.id);
  return true;
}
// function addp(x, i) {
//   $("id").html(i);
//   $("hello").html("hai aadsfsad");
//   alert(document.getElementById("noofitems").value);
//   $("#subform").submit();
// }
function minus() {
  count = Number(document.getElementById("countorders").innerHTML);
  if (count == 0) {
  } else count--;

  localStorage.setItem("count", count);
  console.log(localStorage);
  console.log(count);
  document.getElementById("countorders").innerHTML = count;

  return true;
}

var index = 0;
slide();
function slide() {
  var i;
  var x = document.getElementsByClassName("img");
  for (i = 0; i < x.length; i++) {
    x[i].style.display = "none";
  }
  if (window.index == x.length) {
    window.index = 0;
  }

  console.log(window.index + "iiiiiiiiiiiiiiiii");
  x[window.index].style.display = "block";
  // var y = x[index].src;
  // alert(y);
  // document.getElementById("imgbox").style.backgroundImage =
  // "url('butter_chicken.jfif')";

  index++;
  setTimeout(slide, 3000);
}
