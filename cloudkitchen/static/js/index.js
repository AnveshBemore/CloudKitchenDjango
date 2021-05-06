var count = 0;
setCount();
function setCount() {
  var co = document.getElementById("countorders").innerHTML;
  console.log(co);
  // localStorage.setItem("count", co);
  document.getElementById("countorders").innerHTML = co;
  // document.getElementById("countorders").innerHTML = cou;
  var x = document.getElementById("sign").innerHTML;
  if (x !== "signin") {
    // console.log("xxxxxxxxxxxxxxxxxxxxx");
    localStorage.setItem("uname", x);
  }
  var unam = localStorage.getItem("uname");
  document.getElementById("sign").innerHTML = unam;
  console.log(x + " xxxxxxxxxxxxxxxxxxxxxxx");
  var co = document.getElementById("countorders").innerHTML;
  console.log(co);
  localStorage.setItem("count", co);
  var orde=localStorage.getItem("ordered");
  console.log("nnnnnnnnoooooooffff"+orde);
  if (
    localStorage.getItem("noofitems") === "0" &&
    localStorage.getItem("total")=== "0" && localStorage.getItem("ordered")=== "1"
  ) {
    document.getElementById("countorders").innerHTML = 0;
    console.log("heeeeeeeeeeelllllllllllllllooooooooooo");
  }
}

function plus(x) {
  //   var ele = document.getElementById("countorders");
  //   count = Number(ele.innerHTML);
  count = Number($("#countorders").html());
  count++;
  // alert(v);
  localStorage.setItem("count", count);
  //   ale-rt(count);
  $("#countorders").html(count);
  localStorage.setItem("ordered","0");
  //   var idn="count";
  //  var coinitial=Number( $(`#${idn}`).html());
  //   coinitial++;
  //   $(`#${idn}`).html(coinitial);
  // alert(this.attr("id"));
  // alert(this.)
  // addp(this, this.id);

  return true;
}

function minus() {
  count = Number(document.getElementById("countorders").innerHTML);
  if (count == 0) {
  } else count--;

  localStorage.setItem("count", count);
  localStorage.setItem("ordered","0");
  document.getElementById("countorders").innerHTML = count;
  return true;
}
