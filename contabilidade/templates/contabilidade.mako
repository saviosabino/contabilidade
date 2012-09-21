<link rel="stylesheet" href="${request.static_url('contabilidade:static/pylons.css')}" type="text/css" media="screen" charset="utf-8" />

<h3>Contabilidade do Período: ${contab.periodo}</h3>
Código: ${contab.seq}
<br />
balanço: ${contab.balanco[0]}, crédito: ${contab.balanco[1]}, débito: ${contab.balanco[2]}

<br />
<br />
<p>Créditos:</p>
<table>
    <thead>
        <th style="width:50px">seq</th>
        <th style="width:200px">nome</th>
        <th style="width:100px">período</th>
        <th style="width:100px">valor</th>
    </thead>
    % for cred in contab.creditos:
        <tr style="text-align:center">
            <td>${cred.seq}</td>
            <td>${cred.nome}</td>
            <td>${cred.periodo}</td>
            <td>${cred.valor}</td>

        </tr>
    % endfor
</table>

<br />
<br />
<p>Pagamentos:</p>
<table>
    <thead>
        <th style="width:50px">seq</th>
        <th style="width:200px">nome</th>
        <th style="width:100px">valor</th>
        <th style="width:50px">pago</th>
        <th style="width:300px">tipo</th>
    </thead>
    % for pag in contab.pagamentos:
        <tr style="text-align:center">
            <td>${pag.seq}</td>
            <td>${pag.nome}</td>
            <td>${pag.valor}</td>
            <td>${[u'Não', 'Sim'][pag.pago]}</td>
            <td>${pag.tipo}</td>

        </tr>
    % endfor
</table>



<br />
<br />

${contab}
<br />
<br />

