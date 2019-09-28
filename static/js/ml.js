$(document).ready(function(){
	$('form').on('submit', function(event){
		
		$.ajax({
			type: 'POST',
			url: '/process',
			data: {
				sepalLength1: $('#sepalLength').val(),
				sepalWidth: $('#sepalWidth').val(),
				petalLength: $('#petalLength').val(),
				petalWidth: $('#petalWidth').val()

			},
			success: function(data) {
				$("#result").text(data.prediction);
			}
		});

		event.preventDefault();
	});
});