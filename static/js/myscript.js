// let pudDstr = "<h1>The Main Heading That We want To Render as H1</h1>";
// document.getElementsByTagName("p")[1].innerText= pudDstr;


var getRenData = document.getElementsByClassName("card-text")[0];
console.log(getRenData[1],"Get")
var fkid = getRenData.firstChild;
console.log(fkid,"fkid")
// access the right tag
// var posTag = getRenData[1];

//chnage to text/html

//var htmlString = posTag.innerText;

// now convert
var convertValue = new DOMParser().parseFromString(fkid.innerText, "text/html");

// final render

let nowRenderFinal  = getRenData.innerHTML = convertValue.firstChild.innerHTML;
console.log(nowRenderFinal,"Hello");
	  