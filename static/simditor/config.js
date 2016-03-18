$(function(){
  
    function getCookie(name) {
      var cookieValue = null;
      if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
          var cookie = jQuery.trim(cookies[i]);
          // Does this cookie string begin with the name we want?
          if (cookie.substring(0, name.length + 1) == (name + '=')) {
            cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
            break;
          }
        }
      }
      return cookieValue;
    }
    var csrftoken = getCookie('csrftoken');
  
    toolbar = [ 'title', 'bold', 'italic', 'strikethrough','color',
                '|', 'ol', 'ul', 'indent', 'outdent',
                '|', 'table', 'link', 'image', 'blockquote', 'hr', '|', 'code', 'html', 'markdown'
              ];
    codeLanguages = [
        { name: 'Python', value: 'py prettyprint linenums' },
        { name: 'Bash', value: 'bash  prettyprint linenums' },
        { name: 'PHP', value: 'php  prettyprint linenums' },
        { name: 'CSS', value: 'css  prettyprint linenums' },
        { name: 'SQL', value: 'sql  prettyprint linenums'},
        { name: 'JSON', value: 'json  prettyprint linenums' },
        { name: 'HTML,XML', value: 'html  prettyprint linenums' },
        { name: 'Markdown', value: 'markdown  prettyprint linenums' },
        { name: 'JavaScript', value: 'js  prettyprint linenums' },
    ];
    var editor = new Simditor( {
        textarea : $('#id_content'),
        placeholder : '这里输入内容...',
        toolbar : toolbar,  //工具栏
        codeLanguages : codeLanguages,
        defaultImage : '/static/simditor/img/image.png',
        // 图片上传部分
        upload: {
          url: '/upload/', // 处理图片保存的view地址
          params: { 'csrfmiddlewaretoken': csrftoken},//{ 'csrftoken': 'csrf_token' },  // 解决csrftoken问题， csrftoken是从cookie里获取的csrftoken值
          fileKey: 'img', // 处理图片保存view里，通过img键获取上传的文件对象
          connectionCount: 3,
          leaveConfirm: 'Uploading files...Cancel?'
        },
    });
})