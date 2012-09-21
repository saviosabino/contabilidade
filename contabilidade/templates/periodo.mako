<link rel="stylesheet" href="${request.static_url('contabilidade:static/pylons.css')}" type="text/css" media="screen" charset="utf-8" />
Periodos:
${len(periodo.lista)}
<br/>
<p>Acessar Perído:</p>
<ul>
% for p in periodo.lista:
        <li><a href="/periodo/${p}">${p}</a></li>
% endfor
</ul>
