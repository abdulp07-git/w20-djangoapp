#!/bin/bash

sed -i 's|^\([[:space:]]*repository:[[:space:]]*\).*|\1abdulp07/w20django|' ./${CHART_NAME}/values.yaml

sed -i "s|^\([[:space:]]*tag:[[:space:]]*\).*|\1v${BUILD_NUMBER}|" ./${CHART_NAME}/values.yaml

sed -i "s/^version:.*/version: 0.1.${BUILD_NUMBER}/" ./${CHART_NAME}/Chart.yaml
