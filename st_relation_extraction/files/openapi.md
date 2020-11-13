# 文本关系提取服务 (Text Relationship Extraction Service)

提取文本中的一些特定关系提取和属性提取

## Table of Contents

* [Paths](#paths)
  - [`POST` /tres/v1/attr/money](#op-post-tres-v1-attr-money) 
  - [`GET` /tres/v1/ping](#op-get-tres-v1-ping) 





## Paths


### `POST` /tres/v1/attr/money
<a id="op-post-tres-v1-attr-money" />

> 金额属性







#### Request body
###### application/json



<table>
  <thead>
    <tr>
      <th>Name</th>
      <th>Type</th>
      <th>Description</th>
      <th>Accepted values</th>
    </tr>
  </thead>
  <tbody>
      <tr>
        <td>item <strong>(required)</strong></td>
        <td>
          object
        </td>
        <td></td>
        <td><em>Any</em></td>
      </tr>
      <tr>
        <td>item.text <strong>(required)</strong></td>
        <td>
          string
        </td>
        <td>待分析文本</td>
        <td><em>Any</em></td>
      </tr>
      <tr>
        <td>item.config</td>
        <td>
          object
        </td>
        <td></td>
        <td><em>Any</em></td>
      </tr>
      <tr>
        <td>item.config.show_evidence</td>
        <td>
          boolean
        </td>
        <td>是否返回证据</td>
        <td><em>Any</em></td>
      </tr>
  </tbody>
</table>


##### Example _(generated)_

```json
{
  "item": {
    "text": "合同上写明了借款是1万7千元。"
  }
}
```




#### Responses


##### ▶ 200 - Successful Response

###### Headers
_No headers specified_

###### application/json



<!-- <table>
  <thead>
    <tr>
      <th>Name</th>
      <th>Type</th>
      <th>Description</th>
      <th>Accepted values</th>
    </tr>
  </thead>
  <tbody>
      <tr>
        <td>Response</td>
        <td>
          
        </td>
        <td></td>
        <td><em>Any</em></td>
      </tr>
  </tbody>
</table> -->


##### ▶ 422 - Validation Error

###### Headers
_No headers specified_

###### application/json



<table>
  <thead>
    <tr>
      <th>Name</th>
      <th>Type</th>
      <th>Description</th>
      <th>Accepted values</th>
    </tr>
  </thead>
  <tbody>
      <tr>
        <td>detail</td>
        <td>
          array(object)
        </td>
        <td></td>
        <td><em>Any</em></td>
      </tr>
      <tr>
        <td>detail.loc <strong>(required)</strong></td>
        <td>
          array(string)
        </td>
        <td></td>
        <td><em>Any</em></td>
      </tr>
      <tr>
        <td>detail.msg <strong>(required)</strong></td>
        <td>
          string
        </td>
        <td></td>
        <td><em>Any</em></td>
      </tr>
      <tr>
        <td>detail.type <strong>(required)</strong></td>
        <td>
          string
        </td>
        <td></td>
        <td><em>Any</em></td>
      </tr>
  </tbody>
</table>


##### Example _(generated)_

```json
{
  "detail": [
    {
      "loc": [
        "string"
      ],
      "msg": "string",
      "type": "string"
    }
  ]
}
```

#### Tags

<div class="tags">
  <div class="tags__tag"></div>
</div>
</div>


### `GET` /tres/v1/ping
<a id="op-get-tres-v1-ping" />

> 连接测试









#### Responses


##### ▶ 200 - Successful Response

###### Headers
_No headers specified_

###### application/json



<!-- <table>
  <thead>
    <tr>
      <th>Name</th>
      <th>Type</th>
      <th>Description</th>
      <th>Accepted values</th>
    </tr>
  </thead>
  <tbody>
      <tr>
        <td>Response</td>
        <td>
          
        </td>
        <td></td>
        <td><em>Any</em></td>
      </tr>
  </tbody>
</table> -->



#### Tags

<div class="tags">
  <div class="tags__tag"></div>
</div>
</div>


