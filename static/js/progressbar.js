$(function(){
	
	$('.nav li a').on('click',function(event){
		
		//event.preventDefault();
		$url = $(this).attr('href');
		//alert($url);
		$.ajax({
			type : 'GET',
			url : $url,
			data : {},
			success: function(data){ $('.container').fadeIn(1000); }
		});
		
	});
})