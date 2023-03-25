if [ -z "$OPENAI_TOOLS_PYTHON_DIR" ]
then
    export OPENAI_TOOLS_PYTHON_DIR=$OPENAI_TOOLS_DIR/src/
    export PYTHONPATH=$OPENAI_TOOLS_PYTHON_DIR:$PYTHONPATH
fi


function openai-chatgpt()
{
    python3 -m openaitools.chatgpt.chatcli
}

function openai-chatgpt-screen()
{
    screen -S chatgpt -dm openai-chatgpt
}


function openai-dalle()
{
    python3 -m openaitools.dalle.dallecli $@
}

function openai-chatgpt-english-translate()
{
    python3 -m openaitools.chatgpt.languages.english.translateto $1
}

function openai-chatgpt-french-translate()
{
    python3 -m openaitools.chatgpt.languages.french.translateto $1
}