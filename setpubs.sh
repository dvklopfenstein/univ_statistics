# Use the bibliography in this repo

echo '!!!!!! WARNING: YOU MUST RUN: source setpubs.sh !!!!!!!'
echo 'PUBSCONF BEFORE:' $PUBSCONF
export PUBSCONF=`pwd`/pubs/dot_pubsrc
echo 'PUBSCONF AFTER: ' $PUBSCONF
pubs statistics

echo '!!!!!! TEST PUBSCONF IS SET CORRECTLY BY DOING:!!!!!'
echo 'printenv PUBSCONF'
