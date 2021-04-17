var count = 0;
function plus(x) {
  //   var ele = document.getElementById("countorders");
  //   count = Number(ele.innerHTML);
  count = Number($("#countorders").html());
  count++;

  console.log(count);
  $("#countorders").html(count);
  // alert(this.attr("id"));
  // alert(this.)
  addp(this, this.id);
  return false;
}
function addp(x, i) {
  $("id").html(i);
  $("hello").html("hai aadsfsad");
  alert(document.getElementById("noofitems").value);
  $("#subform").submit();
}
function minus() {
  count = Number(document.getElementById("countorders").innerHTML);
  if (count == 0) {
    count = 0;
  } else count--;
  document.getElementById("countorders").innerHTML = count;

  return false;
}

var index = 0;
slide();
function slide() {
  var i;
  var x = document.getElementsByClassName("img");
  for (i = 0; i < x.length; i++) {
    x[i].style.display = "none";
  }
  if (index >= x.length) {
    index = 0;
  }
  x[index].style.display = "block";
  var y = x[index].src;
  // alert(y);
  document.getElementById("imgbox").style.backgroundImage =
    "url('butter_chicken.jfif')";

  index++;
  setTimeout(slide, 3000);
}
