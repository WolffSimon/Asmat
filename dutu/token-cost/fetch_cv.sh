#!/bin/sh
# Fetches the Common Voice interface strings for English, Georgian and Megrelian at the commit in COMMIT.
# The strings are Mozilla's, under the Mozilla Public License 2.0; they are fetched here, not redistributed.
set -e
COMMIT=$(cat COMMIT)
rm -rf cv-src corpus/cv
git clone -q --filter=blob:none --no-checkout https://github.com/common-voice/common-voice cv-src
git -C cv-src checkout -q "$COMMIT" -- web/locales/common-voice/en web/locales/common-voice/ka web/locales/common-voice/xmf
mkdir -p corpus/cv
cp -r cv-src/web/locales/common-voice/en cv-src/web/locales/common-voice/ka cv-src/web/locales/common-voice/xmf corpus/cv/
rm -rf cv-src
