# Handy commands

* Get a list of AppFlows: `aws appflow list-flows | jq '.flows[].flowName'`
* Create an app flow CFN: `aws appflow describe-flow --flow-name blah | python3 appflowcfn.py`

# TODO

first, do what's fastest
* Source & dest configs - Talk to Rick
* Red shift creation and DDL G:\Shared drives\Team\Technologies & Offerings\AWS\Quickstart
* Spin up KMS, rather than asking
* Create S3 Bucket
