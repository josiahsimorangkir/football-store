function showToast(title, message, type = 'info', duration = 4000) {
    const toast = document.getElementById('toast-component');
    const titleEl = document.getElementById('toast-title');
    const messageEl = document.getElementById('toast-message');
    const iconEl = document.getElementById('toast-icon');

    if (!toast) return;

    // Reset state
    toast.classList.remove('opacity-100', 'translate-y-0', 'scale-100');
    toast.classList.add('opacity-0', 'translate-y-10', 'scale-95');

    // Set default style base
    toast.className = `
        fixed bottom-8 right-8 z-50 flex items-center gap-4 
        bg-white border-l-8 shadow-2xl rounded-2xl 
        p-5 pr-8 w-80 sm:w-96 
        opacity-0 translate-y-10 scale-95 
        transition-all duration-300 ease-out
    `;

    // Theme definitions
    const themes = {
        success: { 
            color: 'text-green-600', 
            bg: 'bg-green-100', 
            border: 'border-green-600', 
            icon: '✅' 
        },
        error: { 
            color: 'text-red-600', 
            bg: 'bg-red-100', 
            border: 'border-red-600', 
            icon: '❌' 
        },
        warning: { 
            color: 'text-yellow-600', 
            bg: 'bg-yellow-100', 
            border: 'border-yellow-600', 
            icon: '⚠️' 
        },
        info: { 
            color: 'text-blue-600', 
            bg: 'bg-blue-100', 
            border: 'border-blue-600', 
            icon: 'ℹ️' 
        },
        normal: { 
            color: 'text-gray-700', 
            bg: 'bg-gray-100', 
            border: 'border-gray-400', 
            icon: '💬' 
        }
    };

    const theme = themes[type] || themes.info;

    // Apply theme to main toast
    toast.classList.add(theme.border);

    // Apply icon style
    iconEl.className = `
        flex items-center justify-center w-12 h-12 rounded-full 
        ${theme.bg} ${theme.color} text-2xl shadow-inner
    `;
    iconEl.textContent = theme.icon;

    // Set text
    titleEl.textContent = title;
    messageEl.textContent = message;

    // Animate show
    requestAnimationFrame(() => {
        toast.classList.remove('opacity-0', 'translate-y-10', 'scale-95');
        toast.classList.add('opacity-100', 'translate-y-0', 'scale-100');
    });

    // Hide after duration
    setTimeout(() => {
        toast.classList.remove('opacity-100', 'translate-y-0', 'scale-100');
        toast.classList.add('opacity-0', 'translate-y-10', 'scale-95');
    }, duration);
}
