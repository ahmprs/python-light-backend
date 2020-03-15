function btnAddClick() {
	let x = parseInt($('#txt_x').val());
	let y = parseInt($('#txt_y').val());
	$.post('../backend/api/add.py', { x, y }, function(d, s) {
		console.log(d);
		$('#spn_res').text(d['res']);
	});
}

function btnSayHello() {
	$.post('../backend/api/sayHello.py', {}, function(d, s) {
		console.log(d);
		$('#spn_say_hello').text(d['res']);
	});
}
