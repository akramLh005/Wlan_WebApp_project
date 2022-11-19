require_once('../vendor/autoload.php');

//twig
Twig_Autoloader::register();
$loader = new Twig_Loader_Filesystem('../app/views');
$twig = new Twig_Environment($loader);
$twig->addFunction(new \Twig_SimpleFunction('asset', function ($asset) {
    // implement whatever logic you need to determine the asset path

    return sprintf('../assets/%s', ltrim($asset, '/'));
}));