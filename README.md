## Key library

https://pkg.go.dev/github.com/bicomsystems/go-libzfs

## OpenTelemetry examples

https://github.com/open-telemetry/opentelemetry-proto/blob/main/examples/metrics.json

## OLTP JSON example (suggested by Perplexity)

```json
{
  "resource": {
    "attributes": {
      "service.name": "your_service_name"
    }
  },
  "metrics": [
    {
      "name": "metric_name",
      "description": "Description of the metric",
      "unit": "unit of measurement",
      "data": {
        "dataPoints": [
          {
            "attributes": {
              "label1": "value1",
              "label2": "value2"
            },
            "startTimeUnixNano": "1234567890000000000",
            "timeUnixNano": "1234567890000000000",
            "value": 42
          }
        ]
      }
    }
  ]
}
```

##  Updates to alloy-config.river (suggested by Perplexity)

```
otelcol.receiver.exec "my_script" {
  command = "/path/to/your/script"
  interval = "60s"
  timeout = "10s"

  env {
    SOME_ENV_VAR = "value"
  }

  output {
    metrics = [otelcol.processor.resourcedetection.default.input]
  }
}
```


