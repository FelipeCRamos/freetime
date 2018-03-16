call plug#begin()

Plug 'tpope/vim-sensible'
Plug 'junegunn/vim-github-dashboard'
Plug 'vim-airline/vim-airline'
Plug 'vim-airline/vim-airline-themes'
Plug 'sheerun/vim-polyglot'
" Plug 'vim-syntastic/syntastic' " It will conflit with Ale
Plug 'w0rp/ale'
Plug 'scrooloose/nerdcommenter'
Plug 'powerline/powerline'
Plug 'rafi/awesome-vim-colorschemes'
Plug 'chriskempson/base16-vim'

set mouse=a
set tabstop=4
set shiftwidth=4
set number
set relativenumber
set smartindent
set paste

let base16colorspace=256

if filereadable(expand("~/.vimrc_background"))
  let base16colorspace=256
  source ~/.vimrc_background
endif

colo base16-tomorrow-night
" Ale settings
let g:airline#extensions#ale#enabled = 1
let g:ale_lint_delay = 1000
let g:ale_lint_on_enter = 0
let g:ale_lint_on_text_changed = 'normal'


" Powerline config
set rtp+=/usr/local/lib/python2.7/site-packages/powerline/bindings/vim
let g:airline_powerline_fonts = 1

" Airline settings
let g:airline_detect_paste=1
let g:airline#extensions#tabline#enabled = 1
let g:airline_theme='tomorrow'

" Syntastic settings
set statusline+=%#warningmsg#
set statusline+=%{SyntasticStatuslineFlag()}
set statusline+=%*

let g:syntastic_always_populate_loc_list = 0
let g:syntastic_auto_loc_list = 0
let g:syntastic_check_on_open = 0
let g:syntastic_check_on_wq = 0

" NERDCommenter settings
" Add spaces after comment delimiters by default
let g:NERDSpaceDelims = 1

" Use compact syntax for prettified multi-line comments
let g:NERDCompactSexyComs = 1

" Align line-wise comment delimiters flush left instead of following code indentation
let g:NERDDefaultAlign = 'left'

" Set a language to use its alternate delimiters by default
let g:NERDAltDelims_java = 1

" Add your own custom formats or override the defaults
let g:NERDCustomDelimiters = { 'c': { 'left': '/**','right': '*/' } }

" Allow commenting and inverting empty lines (useful when commenting a region)
let g:NERDCommentEmptyLines = 1

" Enable trimming of trailing whitespace when uncommenting
let g:NERDTrimTrailingWhitespace = 1

call plug#end()
