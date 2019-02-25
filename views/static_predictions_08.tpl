<html>
  <head>
    <meta charset='utf-8'>
    <title>Гороскоп на сегодня</title>
    <link
      rel="stylesheet"
      href="/css/bootstrap.min.css"
    >
    <script src="/js/jquery-3.3.1.min.js"></script>
  </head>
  <body>
    <div class="container">
      <h1>Что день {{ date }} готовит</h1>

      % if special_date:
      <h2>Сегодня супер особенный день!</h2>
      % end

      <div class="row">
        <div class="col" id="p-0">
          p-0
        </div>
        <div class="col" id="p-1">
          p-1
        </div>
        <div class="col" id="p-2">
          p-2
        </div>
      </div>

      <div class="row">
        <div class="col" id="p-3">
          p-3
        </div>
        <div class="col" id="p-4">
          p-4
        </div>
        <div class="col" id="p-5">
          p-5
        </div>
      </div>
    </div>
  </body>
  <script language="javascript">
    console.log( {{ x }} );

    function set_content_in_divs(paragraphs) {
      
      console.log("entered function")
      console.log(paragraphs)
      
      $.each(paragraphs, function(i, d) {
        p = $("#p-" + i)
        p.html("<p>" + d + "</p>")
        
        console.log("i value: " + i)
        console.log("d value: " + d)
      
      })

      console.log("function done")
    }
    console.log("Before clicking")

    var par = $.getJSON("localhost:8080/api/forecasts")[prophecies];
    $("h1").click(set_content_in_divs());
  </script>
</html>