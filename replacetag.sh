#!/bin/bash
sed -i "s/\(tag:[[:space:]]*\"v\)[0-9]\+\"/\1${BUILD_NUMBER}\"/" ./helm-chart/values.yaml

sed -i "s/^version:.*/version: 0.1.${BUILD_NUMBER}/" ${CHART_NAME}/Chart.yaml
