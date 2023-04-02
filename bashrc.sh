if [ -z "$OPENAI_TOOLS_PYTHON_DIR" ]
then
    export OPENAI_TOOLS_PYTHON_DIR=$OPENAI_TOOLS_DIR/src/
    export PYTHONPATH=$OPENAI_TOOLS_PYTHON_DIR:$PYTHONPATH
fi


function openai-chatgpt()
{
    python3 -m openaitools.chatgpt.chatcli
}

function openai-chatgpt-continue()
{
    chatgpt_dir=$CHATGPT_CHAT_BKP_DIR
    if [ -z "$chatgpt_dir" ]
    then
        chatgpt_dir=$HOME/.chatgpt
    fi

    chatgpt_file=$(find ${chatgpt_dir} -name "*.json" | default-fuzzy-finder)

    python3 -m openaitools.chatgpt.chatcli ${chatgpt_file}
}

function openai-chatgpt-continue-add-file()
{
    chatgpt_dir=$CHATGPT_CHAT_BKP_DIR
    if [ -z "$chatgpt_dir" ]
    then
        chatgpt_dir=$HOME/.chatgpt
    fi

    chatgpt_file=$(find ${chatgpt_dir} -name "*.json" | default-fuzzy-finder)

    attachment_file=$(find . | default-fuzzy-finder)

    python3 -m openaitools.chatgpt.chatcli ${chatgpt_file} ${attachment_file}
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

function openai-chatgpt-japanese-translate()
{
    python3 -m openaitools.chatgpt.languages.japanese.translateto $1
}


function openai-chatgpt-korean-translate()
{
    python3 -m openaitools.chatgpt.languages.korean.translateto $1
}