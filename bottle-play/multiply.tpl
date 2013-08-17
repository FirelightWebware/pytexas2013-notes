<head>
    <title>Multiply!</title>
    <link type="text/css" rel="stylesheet" href="/public/style.css">
</head>
<body>
    <h1>Multiply!</h1>
    <h2>{{ greeting }}</h2>

% try:
%   int(greeting)
<h2>
    {{greeting}} squared is {{int(greeting) * int(greeting)}}
</h2>
% except ValueError:
%   pass
% end

<form method="POST">
    <input type="text" name="a">X
    <input type="text" name="b"><br>
    <input type="submit" value="multiply!">
</form>

</body>
