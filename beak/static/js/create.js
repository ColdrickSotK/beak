var reader = new commonmark.Parser();
var writer = new commonmark.HtmlRenderer();

function setTitle() {
  var title = $('#post-title').val();
  $('.preview .title').html(title);
}
setTitle();

function handleContentInput() {
  var parsed = reader.parse($('#markdown-input').val());
  $('.preview .content').html(writer.render(parsed));
}
handleContentInput();
$('#markdown-input').autogrow({horizontal: false});

$('nav ul li').click(function(){
  $(this).addClass('active').siblings().removeClass('active');
});

$('#markdown-input').on('change input paste', handleContentInput);
$('#post-title').on('change input paste', setTitle);
