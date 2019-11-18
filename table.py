#Table scheme and my notepad! ;)


CREATE TABLE bottlings2 (
    id SERIAL PRIMARY KEY,
    user_date VARCHAR,
    vatting_number VARCHAR,
    bottle_size VARCHAR,
    product VARCHAR,
    back_label VARCHAR,
    qty INTEGER,
    status VARCHAR,
    user_date_completed VARCHAR,
    allow_user_edit BOOLEAN,
    note VARCHAR,
    timestamp TIMESTAMP NOT NULL
);





<div class="container">
    <div class="row">
        <div class="col-sm">
            ID
        </div>
        <div class="col-sm">
            Date added
        </div>
        <div class="col-sm">
            Product
        </div>
        <div class="col-sm">
            Bottle size
        </div>
        <div class="col-sm">
            Label info
        </div>
        <div class="col-sm">
            Quantity
        </div>
        <div class="col-sm">
            Status
        </div>
        <div class="col-sm">
            Date completed
        </div>
        <div class="col-sm">
            Notes
        </div>
    </div>
    {% for bottling_runs in bottling_runs %}
    <div class= "row">
        <div class="col-sm">
            {{bottling_runs.id}}
        </div>
        <div class="col-sm">
            {{bottling_runs.user_date}}
        </div>
        <div class="col-sm">
            {{bottling_runs.vatting_number}}
        </div>
        <div class="col-sm">
            {{bottling_runs.bottle_size}}
        </div>
        <div class="col-sm">
            {{bottling_runs.product}}
        </div>
        <div class="col-sm">
            {{bottling_runs.back_label}}
        </div>
        <div class="col-sm">
            {{bottling_runs.qty}}
        </div>
        <div class="col-sm">
            {{bottling_runs.status}}
        </div>
        <div class="col-sm">
            {{bottling_runs.user_date_completed}}
        </div>
        <div class="col-sm">
            {{bottling_runs.allow_user_edit}}
        </div>
        <div class="col-sm">
            {{bottling_runs.note}}
        </div>
        <div class="col-sm">
            {{bottling_runs.timestamp}}
        </div>
    </div>
    {% endfor %}
</div>




<table class="dashboard-table">
    <tr>
        <th>ID</th>
        <th>User date</th>                        
        <th>Vatting number</th>
        <th>Bottle size</th>
        <th>Product</th>
        <th>Label info</th>
        <th>Qty</th>
        <th>Status</th>
        <th>User completed</th>
        <th>User edit</th>
        <th>Note</th>
        <th>Timestamp</th>
    </tr>
    {% for bottling_runs in bottling_runs %}
    <tr>
        <td>{{bottling_runs.id}}</td>
        <td>{{bottling_runs.user_date}}</td>
        <td>{{bottling_runs.vatting_number}}</td>
        <td>{{bottling_runs.bottle_size}}</td>
        <td>{{bottling_runs.product}}</td>
        <td>{{bottling_runs.back_label}}</td>
        <td>{{bottling_runs.qty}}</td>
        <td>{{bottling_runs.status}}</td>
        <td>{{bottling_runs.user_date_completed}}</td>
        <td>{{bottling_runs.allow_user_edit}}</td>
        <td>{{bottling_runs.note}}</td>
        <td>{{bottling_runs.timestamp}}</td>
    </tr>
    {% endfor %}
</table>