//Disable submit button when no toggle in checked
		let submitBtn = document.querySelector("button");
	document.querySelector(".toggle_button").addEventListener("click", function(){
	  if(this.checked){
		submitBtn.disabled = true;
	  } else {
		submitBtn.disabled = false;
	  }
	});


//toggle between upper and lower
	$(document).ready(function(){
	$("#id_lower_case").on("change",function(){
		if ($("#id_lower_case").prop("checked")==true){
			$("#id_upper_case").prop("checked",false)

		}
	})
	$("#id_upper_case").on("change",function(){
		if ($("#id_upper_case").prop("checked")==true){
			$("#id_lower_case").prop("checked",false)

		}
	})
	})


//validation
	function validateForm() {
 	 var x = document.forms["myform"]["textarea"].value;
 	 if (x == "") {
  		  alert("Please enter any text to proceed");
  	 	 return false;
  }
}