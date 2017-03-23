var reader = new commonmark.Parser();
var writer = new commonmark.HtmlRenderer();

$('.post-row a').click(function(event) {
  event.stopPropagation();
})

$('.post-row').click(function(){
  $(this).addClass('active').siblings().removeClass('active');
  var slug = $(this).find('.post-title').text();
  $.get('/posts/' + slug, function(data, status) {
    var obj = JSON.parse(data);
    var parsed = reader.parse(obj.content);
    $('.preview .content').html(writer.render(parsed));
    $('.preview .title').html(obj.metadata.title);
  });
});
