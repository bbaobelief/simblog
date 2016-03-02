$(function(){
    toolbar = [ 'title', 'bold', 'italic', 'strikethrough','color', 
                '|', 'ol', 'ul', 'indent', 'outdent', 
                '|', 'table', 'link', 'image', 'blockquote', 'hr', '|', 'code', 'html', 'markdown'
              ];
    codeLanguages = [
        { name: 'Python', value: 'py prettyprint linenums' },
        { name: 'Bash', value: 'bash  prettyprint linenums' },
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
            <!-- defaultImage : '/static/simditor/img/image.png', //编辑器插入图片时使用的默认图片 -->
            defaultImage : 'img/image.png', //编辑器插入图片时使用的默认图片
        });
    })