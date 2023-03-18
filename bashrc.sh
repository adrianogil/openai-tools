if [ -z "$OPENAI_TOOLS_PYTHON_DIR" ]
then
    export OPENAI_TOOLS_PYTHON_DIR=$OPENAI_TOOLS_DIR/src/
    export PYTHONPATH=$OPENAI_TOOLS_PYTHON_DIR:$PYTHONPATH
fi


function openai-chatgpt()
{
    python3 -m openaitools.chatgpt.chatcli
}
