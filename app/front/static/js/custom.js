$(document).ready(function(){
	if(document.querySelector("#body").classList == "dark"){
		$("#customSwitch1").attr("checked","checked")
	}
	
	$('.Pesquisar').click(function(){
		$('#buscar').toggle()
		$('.Pesquisar').toggle();
	})
	
	$("#prestbtn").click(function(){
		$("#vagas").hide()
		$("#prest").show()
	})
	$("#vagasbtn").click(function(){
		$("#prest").hide()
		$("#vagas").show()
	})
	
	$(".btn_psw").click(function(){
		var psw = document.querySelectorAll(".psw")
		
		if(psw[0].type === "password"){
			$(".psw").attr("type","text")
			$(".sp_psw").html(" Esconder Senha")
		}else{
			$(".psw").attr('type','password')
			$(".sp_psw").html(" Mostrar Senha")
		}
	})

	$("#senha_2").keyup(function(){
		if($("#senha_2").val().length > 7){
			if($("#senha_1").val() === $("#senha_2").val()){
				$("#senha_erro").hide()
				$("#senha_2").attr("minlength","8")
			}else{
				$("#senha_erro").show()
				$("#senha_2").attr("minlength","256")
			}
		}else{
			$("#senha_erro").hide()
			$("#senha_2").attr("minlength","8")
		}
	})
	$("#senha_1").keyup(function(){
		if($("#senha_2").val()){
			if($("#senha_1").val() === $("#senha_2").val()){
				$("#senha_erro").hide()
				$("#senha_2").attr("minlength","8")
			}else{
				$("#senha_erro").show()
				$("#senha_2").attr("minlength","256")
			}
		}else{
			$("#senha_erro").hide()
			$("#senha_2").attr("minlength","8")
		}
	})
	$('#tel').mask('+55 (99) 99999 9999');
})
/*
const toBase64 = file => new Promise((resolve, reject) => {
    const reader = new FileReader();
    reader.readAsDataURL(file);
    reader.onload = () => resolve(reader.result);
    reader.onerror = error => reject(error);
});

async function Main() {
   const file = document.querySelector('#myfile').files[0];
   return await toBase64(file)
}
*/

function tema(){
	if(document.querySelector("#body").classList == "dark")
	{	document.querySelector('#body').classList.remove('dark');
		localStorage.removeItem('darkmode')
	}else{
		localStorage.setItem('darkmode','on')
		document.querySelector('#body').classList.add('dark');
	}
}