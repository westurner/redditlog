#!/bin/bash

_USERNAME=$1

_PREFIX='.' # ${_WRD}

_DATE=$(date +%Y%m%d%H%M)
_DATADIR="${_PREFIX}/data/${_DATE}" #
_HTMLDIR="${_DATADIR}"
_HTMLINDEX="${_HTMLDIR}/index.html"
_JSONLINK="${_DATADIR}/redemdata.json"
_JSONDATA="${_DATADIR}/redemdata.${_DATE}.json"
_STATICFILES="${_PREFIX}/redem/static/"
_REDEM_BIN="redem" # 

mkdir -p ${_DATADIR} ${_HTMLDIR}
rsync -avpr ${_STATICFILES} ${_HTMLDIR}

${_REDEM_BIN} --verbose \
    --backup \
    --json="${_JSONDATA}" \
    --html \
    --html-output="${_HTMLINDEX}" \
    ${_USERNAME} \
&& \
rm -f ${_JSONLINK} \
&& \
ln -s ${_JSONDATA} ${_JSONLINK}

_LAUNCH=$2
if [ -n ${_LAUNCH} ]; then
    chromium-browser ${_HTMLINDEX}
fi
