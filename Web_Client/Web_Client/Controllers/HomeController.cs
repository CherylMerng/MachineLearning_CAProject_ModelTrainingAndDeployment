using Microsoft.AspNetCore.Mvc;
using System.Diagnostics;
using Web_Client.Models;

namespace Web_Client.Controllers
{
    public class HomeController : Controller
    {

        public IActionResult Index()
        {
            return View();
        }

        public IActionResult Privacy()
        {
            return View();
        }

        [HttpPost]
        public async Task<IActionResult> Model1(float a, float b, float c, float d)
        {
            var httpClient = new HttpClient();

            var URL = $"http://localhost:8070/model1?a={a}&b={b}&c={c}&d={d}";
            var response = await httpClient.GetAsync(URL);
            var result = await response.Content.ReadAsStringAsync();

            TempData["result"] = result;

            return RedirectToAction("Index");
        }

    }
}