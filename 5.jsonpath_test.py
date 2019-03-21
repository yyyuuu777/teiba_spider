#coding:utf-8
import jsonpath


# data = {"key1":{"key2":{"key3":{"key4":{"key5":{"key6":{"key7":"python37"}}}}}}}
#
# print(data["key1"]["key2"]["key3"]["key4"]["key5"]["key6"]["key7"])
#
#
# # jsonpath返回的结果为列表
# print(jsonpath.jsonpath(data, '$.key1.key2.key3.key4.key5.key6.key7')[0])
# print(jsonpath.jsonpath(data, '$..key7')[0])

book_dict = {
  "store": {
    "book": [
      { "category": "reference",
        "author": "Nigel Rees",
        "title": "Sayings of the Century",
        "price": 8.95
      },
      { "category": "fiction",
        "author": "Evelyn Waugh",
        "title": "Sword of Honour",
        "price": 12.99
      },
      { "category": "fiction",
        "author": "Herman Melville",
        "title": "Moby Dick",
        "isbn": "0-553-21311-3",
        "price": 8.99
      },
      { "category": "fiction",
        "author": "J. R. R. Tolkien",
        "title": "The Lord of the Rings",
        "isbn": "0-395-19395-8",
        "price": 22.99
      }
    ],
    "bicycle": {
      "color": "red",
      "price": 19.95
    }
  }
}

print(jsonpath.jsonpath(book_dict, '$..color')[0])
print(jsonpath.jsonpath(book_dict, '$..price'))