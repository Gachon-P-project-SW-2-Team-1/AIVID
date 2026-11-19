#streamlit>=1.66.1
import streamlit as st
import textwrap

# ==================================================
# 1. PAGE CONFIG
# ==================================================

st.set_page_config(
    page_title="EditAI Studio",
    page_icon="E",
    layout="wide",
    initial_sidebar_state="expanded"
)


# ==================================================
# 2. SESSION STATE
# ==================================================

if "uploaded_file" not in st.session_state:
    st.session_state.uploaded_file = None

if "messages" not in st.session_state:
    st.session_state.messages = []

if "selected_menu" not in st.session_state:
    st.session_state.selected_menu = "프로젝트 작업실"


# ==================================================
# 3. CUSTOM CSS
# ==================================================

st.markdown("""
<style>

/* Global */
.stApp {
    background-color: #212121;
    color: #ECECEC;
}

[data-testid="stHeader"] {
    background: transparent;
}

[data-testid="stMainBlockContainer"] {
    max-width: 1100px;
    padding-top: 2.5rem;
    padding-bottom: 7rem;
}

h1, h2, h3, h4 {
    color: #F5F5F5;
    letter-spacing: -0.7px;
}

/* Sidebar */
section[data-testid="stSidebar"] {
    background-color: #171717;
    border-right: 1px solid #303030;
}

section[data-testid="stSidebar"] > div {
    padding-top: 2rem;
}

.sidebar-brand {
    font-size: 22px;
    font-weight: 700;
    letter-spacing: -0.8px;
    color: #F5F5F5;
    margin-bottom: 4px;
}

.sidebar-caption {
    font-size: 11px;
    color: #858585;
    letter-spacing: 1px;
    margin-bottom: 25px;
}

section[data-testid="stSidebar"] [data-testid="stRadio"] label {
    padding: 9px 12px;
    border-radius: 8px;
    color: #D0D0D0;
}

section[data-testid="stSidebar"] [data-testid="stRadio"] label:hover {
    background-color: #292929;
}

/* Welcome Screen */
.welcome-container {
    text-align: center;
    padding: 105px 20px 40px 20px;
}

.welcome-title {
    font-size: 34px;
    font-weight: 600;
    letter-spacing: -1.3px;
    color: #F5F5F5;
    margin-bottom: 14px;
}

.welcome-description {
    font-size: 15px;
    color: #999999;
    line-height: 1.8;
}

/* Cards */
div[data-testid="stVerticalBlockBorderWrapper"] {
    background-color: #292929;
    border: 1px solid #3A3A3A;
    border-radius: 14px;
}

/* Buttons */
.stButton > button {
    border-radius: 9px;
    border: 1px solid #414141;
    background-color: #292929;
    color: #EAEAEA;
    transition: all 0.2s ease;
}

.stButton > button:hover {
    background-color: #383838;
    border-color: #666666;
    color: white;
}

/* Chat */
[data-testid="stChatMessage"] {
    background-color: transparent;
    border: none;
    padding: 12px 0;
}

[data-testid="stChatInput"] {
    background-color: #2B2B2B;
    border: 1px solid #484848;
    border-radius: 18px;
    padding: 5px;
}

[data-testid="stChatInput"] textarea {
    color: #F5F5F5;
}

[data-testid="stChatInput"] textarea::placeholder {
    color: #888888;
}

/* File Uploader */
[data-testid="stFileUploader"] {
    background-color: #292929;
    border-radius: 12px;
}

/* Metrics */
[data-testid="stMetric"] {
    background-color: #292929;
    padding: 15px;
    border-radius: 10px;
    border: 1px solid #3A3A3A;
}

/* Divider */
hr {
    border-color: #353535;
}

/* Text */
.stCaption {
    color: #929292;
}

/* Hide Streamlit Branding */
#MainMenu {
    visibility: hidden;
}

footer {
    visibility: hidden;
}

</style>
""", unsafe_allow_html=True)


# ==================================================
# 4. SIDEBAR
# ==================================================

with st.sidebar:

    st.markdown(
        '<div class="sidebar-brand">EditAI Studio</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="sidebar-caption">'
        'AI VIDEO EDITING WORKSPACE'
        '</div>',
        unsafe_allow_html=True
    )

    st.divider()

    st.markdown(
        """
        <p style="
            font-size:11px;
            color:#777;
            font-weight:600;
            letter-spacing:1px;
        ">
            WORKSPACE
        </p>
        """,
        unsafe_allow_html=True
    )

    menu_items = [
        "프로젝트 작업실",
        "미디어 라이브러리",
        "편집 히스토리",
        "설정"
    ]

    selected_menu = st.radio(
        "Navigation",
        menu_items,
        index=menu_items.index(
            st.session_state.selected_menu
        ),
        label_visibility="collapsed"
    )

    st.session_state.selected_menu = selected_menu

    st.divider()

    st.markdown(
        """
        <div style="
            font-size:12px;
            color:#777;
            letter-spacing:0.5px;
        ">
            EDITAI STUDIO · BETA
        </div>
        """,
        unsafe_allow_html=True
    )


# ==================================================
# 5. PROJECT WORKSPACE
# ==================================================

if selected_menu == "프로젝트 작업실":

    st.markdown(
        """
        <div style="
            font-size:13px;
            color:#999;
            margin-bottom:10px;
        ">
            PROJECT WORKSPACE
        </div>
        """,
        unsafe_allow_html=True
    )

    # Video Preview

    if st.session_state.uploaded_file is not None:

        st.markdown("### 첨부된 영상")

        col_video, col_info = st.columns([1.5, 1])

        with col_video:

            st.video(st.session_state.uploaded_file)

        with col_info:

            st.markdown("#### 파일 정보")

            st.metric(
                "파일명",
                st.session_state.uploaded_file.name
            )

            st.metric(
                "파일 크기",
                f"{st.session_state.uploaded_file.size / (1024 * 1024):.2f} MB"
            )

            if st.button(
                "영상 제거",
                use_container_width=True
            ):

                st.session_state.uploaded_file = None
                st.rerun()

        st.divider()

    # Welcome Screen

    if (
            len(st.session_state.messages) == 0
            and st.session_state.uploaded_file is None
    ):

        st.html("""
            <div style="
                text-align: center;
                padding: 105px 20px 40px 20px;
            ">
                <div style="
                    font-size: 34px;
                    font-weight: 600;
                    letter-spacing: -1.3px;
                    color: #F5F5F5;
                    margin-bottom: 14px;
                ">
                    무엇을 편집해 드릴까요?
                </div>

                <div style="
                    font-size: 15px;
                    color: #999999;
                    line-height: 1.8;
                ">
                    영상과 원하는 편집 내용을 입력하면<br>
                    AI가 요청을 분석하고 편집 작업을 준비합니다.
                </div>
            </div>
        """)

        st.markdown("#### 시작하기")

        col1, col2 = st.columns(2)

        # Cut Editing Card

        with col1:

            with st.container(border=True):

                st.markdown("**컷 편집 및 트리밍**")

                st.caption(
                    "원하는 시간 구간을 지정하여 "
                    "불필요한 장면을 제거합니다."
                )

                if st.button(
                    "컷 편집 시작",
                    key="cut_example",
                    use_container_width=True
                ):

                    st.session_state.messages.append({
                        "role": "user",
                        "content": (
                            "3초부터 15초까지 구간만 "
                            "잘라서 추출해 줘."
                        )
                    })

                    st.rerun()

        # Subtitle Card

        with col2:

            with st.container(border=True):

                st.markdown("**자동 자막 생성**")

                st.caption(
                    "영상의 음성을 분석하여 "
                    "자동으로 자막을 생성합니다."
                )

                if st.button(
                    "자막 생성 시작",
                    key="subtitle_example",
                    use_container_width=True
                ):

                    st.session_state.messages.append({
                        "role": "user",
                        "content": (
                            "영상 전체 오디오를 분석해서 "
                            "자막을 생성해 줘."
                        )
                    })

                    st.rerun()

    # Chat History

    for message in st.session_state.messages:

        with st.chat_message(message["role"]):

            st.markdown(message["content"])

    # Chat Input + File Attachment

    chat_value = st.chat_input(
        "편집하고 싶은 내용을 입력하세요...",
        accept_file=True,
        file_type=["mp4", "mov", "avi"]
    )

    if chat_value:

        # File Attachment

        attached_files = getattr(
            chat_value,
            "files",
            []
        )

        if attached_files:

            st.session_state.uploaded_file = attached_files[0]

        # User Prompt

        prompt = chat_value.text.strip()

        if prompt:

            st.session_state.messages.append({
                "role": "user",
                "content": prompt
            })

            # Temporary Assistant Response

            response = (
                f"**요청 내용**\n\n"
                f"{prompt}\n\n"
                "요청을 확인했습니다. "
                "편집 계획을 분석하고 처리할 준비가 되었습니다."
            )

            st.session_state.messages.append({
                "role": "assistant",
                "content": response
            })

        st.rerun()


# ==================================================
# 6. MEDIA LIBRARY
# ==================================================

elif selected_menu == "미디어 라이브러리":

    st.title("미디어 라이브러리")

    st.caption(
        "업로드된 원본 영상과 편집 결과물을 관리합니다."
    )

    if st.session_state.uploaded_file is not None:

        st.markdown("#### 업로드된 미디어")

        st.write(
            st.session_state.uploaded_file.name
        )

        st.video(
            st.session_state.uploaded_file
        )

    else:

        st.info(
            "아직 업로드된 미디어가 없습니다."
        )


# ==================================================
# 7. EDIT HISTORY
# ==================================================

elif selected_menu == "편집 히스토리":

    st.title("편집 히스토리")

    st.caption(
        "지금까지 진행한 영상 편집 요청을 확인합니다."
    )

    if st.session_state.messages:

        for i, message in enumerate(
            st.session_state.messages
        ):

            if message["role"] == "user":

                with st.container(border=True):

                    st.caption(
                        f"EDIT REQUEST {i + 1}"
                    )

                    st.write(
                        message["content"]
                    )

    else:

        st.info(
            "아직 편집 기록이 없습니다."
        )


# ==================================================
# 8. SETTINGS
# ==================================================

elif selected_menu == "설정":

    st.title("설정")

    st.caption(
        "AI 모델 및 편집 환경을 관리합니다."
    )

    st.markdown("#### AI 모델")

    st.selectbox(
        "언어 모델",
        ["LLM API 연동 예정"]
    )

    st.markdown("#### 영상 편집")

    st.selectbox(
        "기본 출력 형식",
        ["MP4"]
    )

    st.selectbox(
        "기본 자막 형식",
        ["ASS", "SRT"]
    )

    st.markdown("#### 시스템")

    st.caption(
        "모델 및 API 연결 설정은 "
        "백엔드 연동 단계에서 구현합니다."
    )
