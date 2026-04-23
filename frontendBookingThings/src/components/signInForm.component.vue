<template>
    <main class="grow flex items-center justify-center px-6 py-16 bg-base-200">
        <div class="w-full max-w-md">

            <!-- Brand -->
            <div class="flex justify-center mb-12">
                <router-link to="/" class="text-4xl font-bold text-secondary tracking-tight">BookingThings</router-link>
            </div>

            <!-- Card -->
            <div class="card bg-base-100 shadow-xl border border-base-300">
                <div class="card-body p-8">

                    <header class="mb-6">
                        <h1 class="card-title text-3xl font-bold text-base-content mb-1">
                            Bienvenido de Nuevo
                        </h1>
                        <p class="text-sm text-base-content/70">
                            Ingresa tus datos para continuar
                        </p>
                    </header>

                    <form class="space-y-4">

                        <!-- Email -->
                        <div class="form-control w-full">
                            <label class="label pt-0" for="email">
                                <span class="label-text font-semibold text-base-content/70">
                                    Correo
                                </span>
                            </label>

                            <label class="input input-bordered flex items-center gap-3 focus-within:outline-secondary w-full">
                                <span class="material-symbols-outlined text-base-content/50 text-[20px]">mail</span>
                                <input id="email" type="email" placeholder="name@company.com"
                                    class="grow border-none focus:outline-none" />
                            </label>
                        </div>

                        <!-- Password -->
                        <div class="form-control w-full">
                            <div class="flex justify-between items-center mb-1">
                                <label class="label p-0" for="password">
                                    <span class="label-text font-semibold text-base-content/70">
                                        Contraseña
                                    </span>
                                </label>
                            </div>

                            <label class="input input-bordered flex items-center gap-3 focus-within:outline-primary w-full">
                                <span class="material-symbols-outlined text-base-content/50 text-[20px]">
                                    lock
                                </span>
                                <input id="password" type="password" placeholder="••••••••"
                                    class="grow border-none focus:outline-none" />
                            </label>
                        </div>

                        <!-- Button -->
                        <button class="btn btn-secondary w-full mt-4 normal-case text-white font-semibold" type="submit">
                            Iniciar Sesión
                            <span class="material-symbols-outlined text-[18px]">arrow_forward</span>
                        </button>

                    </form>

                    <footer class="mt-8 text-center">
                        <p class="text-sm text-base-content/70">
                            No tienes una cuenta?
                            <router-link class="text-secondary font-bold hover:underline" to="/signup">
                                Regístrate
                            </router-link>
                        </p>
                    </footer>

                </div>
            </div>

        </div>
    </main>
</template>