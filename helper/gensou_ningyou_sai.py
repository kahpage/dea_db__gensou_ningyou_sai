# Notes:
import sys
import json
from pathlib import Path
from typing import Any

# Add project root to sys.path (find the directory containing db_structs.py)
_root = Path(__file__).resolve().parent
while _root.parent != _root:
    if (_root / "db_structs.py").exists():
        if str(_root) not in sys.path:
            sys.path.append(str(_root))
        break
    _root = _root.parent

from db_structs import (
    Medium,
    Circle,
    Event,
    EventGroup,
    Source,
    ReliabilityTypes,
    OriginTypes,
    Location,
)

RT, OT = ReliabilityTypes, OriginTypes

PATH_HELPER = Path(__file__).parent
PATH_EVENT_GROUP = PATH_HELPER.parent
PATH_MEDIA = PATH_EVENT_GROUP / "media"


def retrieve_circles(event_name: str) -> list[Circle]:
    """Retrieve circles of given event. In the circle file has not been created, execute the creation script first."""
    circles_json_path = PATH_HELPER / event_name / "circles.json"
    if not circles_json_path.exists():
        print(
            f"Circle file for {event_name} not found, running the creation script ..."
        )
        creation_script_path = PATH_HELPER / event_name / "main.py"
        if not creation_script_path.exists():
            raise FileNotFoundError(
                f"Creation script for {event_name} not found at {creation_script_path}"
            )
        # Import main() from the creation script and execute
        import importlib.util

        spec = importlib.util.spec_from_file_location(
            f"{event_name}.main", creation_script_path
        )
        if spec and spec.loader:
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)
            if hasattr(module, "main"):
                module.main()

        if not circles_json_path.exists():
            raise FileNotFoundError(
                f"Creation script {creation_script_path} failed to create {circles_json_path}"
            )

    with circles_json_path.open("r", encoding="utf-8") as f:
        circles_raw = json.load(f)
    return [Circle.load_from_json(c) for c in circles_raw]


if __name__ == "__main__":
    events: list[Event] = []
    disabled_events: list[int | str] = []

    thwikicc = "https://thwiki.cc/%E5%B9%BB%E6%83%B3%E4%BA%BA%E5%BD%A2%E7%A5%AD"

    i = "u"  # ==== gensou_ningyou_sai u ====
    if i not in disabled_events:
        event_name = f"gensou_ningyou_sai{i}"
        print(f"Processing {event_name} ...")

        media_ = [
            Medium(
                "u_20130102064718_合同ちらし2.jpg",
                [
                    Source(
                        "https://web.archive.org/web/20130102064718/http://yougakudann.onlyevent.info/",
                        (ReliabilityTypes.Reliable, OriginTypes.Official),
                    )
                ],
            ),
            Medium(
                "u_530px-幻想人形祭1目录.jpg",
                [Source(thwikicc, (ReliabilityTypes.Likely, OriginTypes.External))],
            ),
            # Medium("", [Source("", (RT.Reliable, OT.Official))]),
            # Medium("", [Source("", (RT.Reliable, OT.Official))]),
        ]
        locations = [
            Location(
                coordinates=(35.5352689, 139.6991018),
                address="66-20 Horikawacho, Saiwai Ward, Kawasaki, Kanagawa 212-0013, Japan",
                description="川崎市産業振興会館",
                sources=[
                    Source(
                        "https://web.archive.org/web/20140307211133/http://yougakudan.blogspot.jp/2013/03/blog-post_26.html",
                        (ReliabilityTypes.Reliable, OriginTypes.OfficialExt),
                    )
                ],
                # comments=None,
                imageUrl="https://lh3.googleusercontent.com/gps-cs-s/AHRPTWnWztJ2ppoe3w-RXwZKQrT3vkgEbIN62FGlT7NE7zuGU7eM3ofV9HW_XPJIhG_gdXsqJye8REtNEDXEuXtA4hNE6eBFPNp2sgCSTD6dXYj3of4yaxjAaBFGG8WNY2Pr-rM431y9Sf2f9Zg=s0?imgmax=0",
                url="https://maps.app.goo.gl/GBVsEToTAegdTRpK8",
            ),
        ]
        event = Event(
            aliases=[
                "幻想人形祭・卯",
                "Gensou Ningyou Sai U",
                "幻想人形祭(1st)",
                "Gensou Ningyou Sai (1st)",
            ],
            dates="2013.04.21",
            circles=[],
            media=media_,
            sources=[
                Source(
                    "Date: https://web.archive.org/web/20140307211133/http://yougakudan.blogspot.jp/2013/03/blog-post_26.html",
                    (ReliabilityTypes.Reliable, OriginTypes.Official),
                ),
                Source(
                    "Participating circles: https://web.archive.org/web/20140307202447/http://yougakudan.blogspot.jp/",
                    (ReliabilityTypes.Reliable, OriginTypes.Official),
                ),
            ],
            locations=locations,
            description="Simultaneous to 幺樂団カァニバル！4.",
            # comments=None,
            last_edited="2026.10.18",
        )

        # Retrieve circles
        event.circles = retrieve_circles(event_name)
        events.append(event)

    i = "chou"  # ==== gensou_ningyou_sai chou ====
    if i not in disabled_events:
        event_name = f"gensou_ningyou_sai{i}"
        print(f"Processing {event_name} ...")

        media_ = [
            Medium(
                "chou_20140508160625_チラシ_2.jpg",
                [
                    Source(
                        "https://web.archive.org/web/20140508160625/http://yougakudann.onlyevent.info/",
                        (ReliabilityTypes.Reliable, OriginTypes.Official),
                    )
                ],
            ),
            # Medium("", [Source("", (RT.Reliable, OT.Official))]),
            # Medium("", [Source("", (RT.Reliable, OT.Official))]),
        ]
        locations = [
            Location(
                coordinates=(35.5352689, 139.6991018),
                address="66-20 Horikawacho, Saiwai Ward, Kawasaki, Kanagawa 212-0013, Japan",
                description="川崎市産業振興会館",
                sources=[
                    Source(
                        "https://web.archive.org/web/20160129155153/http://yougakudan.blogspot.jp/2013/03/blog-post.html",
                        (ReliabilityTypes.Reliable, OriginTypes.OfficialExt),
                    )
                ],
                # comments=None,
                imageUrl="https://lh3.googleusercontent.com/gps-cs-s/AHRPTWnWztJ2ppoe3w-RXwZKQrT3vkgEbIN62FGlT7NE7zuGU7eM3ofV9HW_XPJIhG_gdXsqJye8REtNEDXEuXtA4hNE6eBFPNp2sgCSTD6dXYj3of4yaxjAaBFGG8WNY2Pr-rM431y9Sf2f9Zg=s0?imgmax=0",
                url="https://maps.app.goo.gl/GBVsEToTAegdTRpK8",
            ),
        ]
        event = Event(
            aliases=[
                "幻想人形祭・長",
                "Gensou Ningyou Sai Chou",
                "幻想人形祭(2nd)",
                "Gensou Ningyou Sai (2nd)",
            ],
            dates="2014.09.14",
            circles=[],
            media=media_,
            sources=[
                Source(
                    "Date, Participating circles: https://web.archive.org/web/20160129155153/http://yougakudan.blogspot.jp/2013/03/blog-post.html",
                    (ReliabilityTypes.Reliable, OriginTypes.Official),
                ),
            ],
            locations=locations,
            description="Simultaneous to 幺樂団カァニバル！5.",
            comments=None,
            last_edited="2026.10.18",
        )

        # Retrieve circles
        event.circles = retrieve_circles(event_name)
        events.append(event)

    i = "shimo"  # ==== gensou_ningyou_sai shimo ====
    if i not in disabled_events:
        event_name = f"gensou_ningyou_sai{i}"
        print(f"Processing {event_name} ...")

        media_ = [
            Medium(
                "shimo_20160826174801_チラシ統合版.jpg",
                [
                    Source(
                        "https://web.archive.org/web/20160826174801/http://yougakudann.onlyevent.info/",
                        (ReliabilityTypes.Reliable, OriginTypes.Official),
                    )
                ],
            ),
            Medium(
                "shimo_配置図.jpg",
                [
                    Source(
                        "https://web.archive.org/web/20161116020013/http://yougakudan.blogspot.jp/2016/10/6.html",
                        (RT.Reliable, OT.Official),
                    )
                ],
            ),
            # Medium("", [Source("", (RT.Reliable, OT.Official))]),
            # Medium("", [Source("", (RT.Reliable, OT.Official))]),
        ]
        locations = [
            Location(
                coordinates=(35.5352689, 139.6991018),
                address="66-20 Horikawacho, Saiwai Ward, Kawasaki, Kanagawa 212-0013, Japan",
                description="川崎市産業振興会館",
                sources=[
                    Source(
                        "https://web.archive.org/web/20160818114141/http://yougakudan.blogspot.jp/2013/03/blog-post.html",
                        (ReliabilityTypes.Reliable, OriginTypes.OfficialExt),
                    )
                ],
                # comments=None,
                imageUrl="https://lh3.googleusercontent.com/gps-cs-s/AHRPTWnWztJ2ppoe3w-RXwZKQrT3vkgEbIN62FGlT7NE7zuGU7eM3ofV9HW_XPJIhG_gdXsqJye8REtNEDXEuXtA4hNE6eBFPNp2sgCSTD6dXYj3of4yaxjAaBFGG8WNY2Pr-rM431y9Sf2f9Zg=s0?imgmax=0",
                url="https://maps.app.goo.gl/GBVsEToTAegdTRpK8",
            ),
        ]
        event = Event(
            aliases=[
                "幻想人形祭・霜",
                "Gensou Ningyou Sai Shimo",
                "幻想人形祭(3rd)",
                "Gensou Ningyou Sai (3rd)",
            ],
            dates="2016.11.12",
            circles=[],
            media=media_,
            sources=[
                Source(
                    "Date: https://web.archive.org/web/20160818114141/http://yougakudan.blogspot.jp/2013/03/blog-post.html",
                    (ReliabilityTypes.Reliable, OriginTypes.Official),
                ),
                Source(
                    "Participating circles: https://web.archive.org/web/20161116020013/http://yougakudan.blogspot.jp/2016/10/6.html",
                    (ReliabilityTypes.Guess, OriginTypes.Official),
                ),
            ],
            locations=locations,
            description="Simultaneous to 幺樂団カァニバル！6.",
            # comments=None,
            last_edited="2026.10.18",
        )

        # Retrieve circles
        event.circles = retrieve_circles(event_name)
        events.append(event)

    i = 1  # ==== gensou_ningyou_sai 1 ====
    if i not in disabled_events:
        event_name = f"gensou_ningyou_sai{i}"
        print(f"Processing {event_name} ...")

        media_ = [
            Medium(
                "01_20171021125833_hp20171111.jpg",
                [
                    Source(
                        "https://web.archive.org/web/20171021125833/http://yougakudann.onlyevent.info/",
                        (ReliabilityTypes.Reliable, OriginTypes.Official),
                    )
                ],
            ),
            # Medium("", [Source("", (RT.Reliable, OT.Official))]),
            # Medium("", [Source("", (RT.Reliable, OT.Official))]),
        ]
        locations = [
            Location(
                coordinates=(35.5352689, 139.6991018),
                address="66-20 Horikawacho, Saiwai Ward, Kawasaki, Kanagawa 212-0013, Japan",
                description="川崎市産業振興会館",
                sources=[
                    Source(
                        "https://web.archive.org/web/20171023135929/http://yougakudan.blogspot.jp/2016/10/7.html",
                        (ReliabilityTypes.Reliable, OriginTypes.OfficialExt),
                    )
                ],
                # comments=None,
                imageUrl="https://lh3.googleusercontent.com/gps-cs-s/AHRPTWnWztJ2ppoe3w-RXwZKQrT3vkgEbIN62FGlT7NE7zuGU7eM3ofV9HW_XPJIhG_gdXsqJye8REtNEDXEuXtA4hNE6eBFPNp2sgCSTD6dXYj3of4yaxjAaBFGG8WNY2Pr-rM431y9Sf2f9Zg=s0?imgmax=0",
                url="https://maps.app.goo.gl/GBVsEToTAegdTRpK8",
            ),
        ]
        event = Event(
            aliases=[
                "幻想人形祭",
                "Gensou Ningyou Sai",
                "幻想人形祭1",
                "Gensou Ningyou Sai 1",
                "幻想人形祭(4th)",
                "Gensou Ningyou Sai (4th)",
            ],
            dates="2017.11.11",
            circles=[],
            media=media_,
            sources=[
                Source(
                    "Date, Participating circles: https://web.archive.org/web/20171023135929/http://yougakudan.blogspot.jp/2016/10/7.html",
                    (ReliabilityTypes.Reliable, OriginTypes.Official),
                ),
            ],
            locations=locations,
            description="Simultaneous to 幺樂団カァニバル！7.",
            # comments=None,
            last_edited="2026.10.18",
        )

        # Retrieve circles
        event.circles = retrieve_circles(event_name)
        events.append(event)

    i = 2  # ==== gensou_ningyou_sai2 ====
    if i not in disabled_events:
        event_name = f"gensou_ningyou_sai{i}"
        print(f"Processing {event_name} ...")

        media_ = [
            # Medium("", [Source("", (RT.Reliable, OT.Official))]),
            # Medium("", [Source("", (RT.Reliable, OT.Official))]),
            # Medium("", [Source("", (RT.Reliable, OT.Official))]),
        ]
        locations = [
            Location(
                coordinates=(35.5352689, 139.6991018),
                address="66-20 Horikawacho, Saiwai Ward, Kawasaki, Kanagawa 212-0013, Japan",
                description="川崎市産業振興会館",
                sources=[
                    Source(
                        "https://web.archive.org/web/20181124073957/http://yougakudan.blogspot.com/",
                        (ReliabilityTypes.Reliable, OriginTypes.OfficialExt),
                    )
                ],
                # comments=None,
                imageUrl="https://lh3.googleusercontent.com/gps-cs-s/AHRPTWnWztJ2ppoe3w-RXwZKQrT3vkgEbIN62FGlT7NE7zuGU7eM3ofV9HW_XPJIhG_gdXsqJye8REtNEDXEuXtA4hNE6eBFPNp2sgCSTD6dXYj3of4yaxjAaBFGG8WNY2Pr-rM431y9Sf2f9Zg=s0?imgmax=0",
                url="https://maps.app.goo.gl/GBVsEToTAegdTRpK8",
            ),
        ]
        event = Event(
            aliases=[
                "幻想人形祭2",
                "Gensou Ningyou Sai 2",
                "幻想人形祭(5th)",
                "Gensou Ningyou Sai (5th)",
            ],
            dates="2018.09.22",
            circles=[],
            media=media_,
            sources=[
                Source(
                    "Date, Participating circles: https://web.archive.org/web/20181124073957/http://yougakudan.blogspot.com/",
                    (ReliabilityTypes.Reliable, OriginTypes.Official),
                ),
            ],
            locations=locations,
            description="Simultaneous to 幺樂団カァニバル！8.",
            # comments=None,
            last_edited="2026.10.18",
        )

        # Retrieve circles
        event.circles = retrieve_circles(event_name)
        events.append(event)

    i = 3  # ==== gensou_ningyou_sai3 ====
    if i not in disabled_events:
        event_name = f"gensou_ningyou_sai{i}"
        print(f"Processing {event_name} ...")

        media_ = [
            # Medium("", [Source("", (RT.Reliable, OT.Official))]),
            # Medium("", [Source("", (RT.Reliable, OT.Official))]),
            # Medium("", [Source("", (RT.Reliable, OT.Official))]),
        ]
        locations = [
            Location(
                coordinates=(35.5352689, 139.6991018),
                address="66-20 Horikawacho, Saiwai Ward, Kawasaki, Kanagawa 212-0013, Japan",
                description="川崎市産業振興会館",
                sources=[
                    Source(
                        "https://web.archive.org/web/20251107154156/http://yougakudan.blogspot.com/2016/10/blog-post_24.html",
                        (ReliabilityTypes.Reliable, OriginTypes.OfficialExt),
                    )
                ],
                # comments=None,
                imageUrl="https://lh3.googleusercontent.com/gps-cs-s/AHRPTWnWztJ2ppoe3w-RXwZKQrT3vkgEbIN62FGlT7NE7zuGU7eM3ofV9HW_XPJIhG_gdXsqJye8REtNEDXEuXtA4hNE6eBFPNp2sgCSTD6dXYj3of4yaxjAaBFGG8WNY2Pr-rM431y9Sf2f9Zg=s0?imgmax=0",
                url="https://maps.app.goo.gl/GBVsEToTAegdTRpK8",
            ),
        ]
        event = Event(
            aliases=[
                "幻想人形祭3",
                "Gensou Ningyou Sai 3",
                "幻想人形祭(6th)",
                "Gensou Ningyou Sai (6th)",
            ],
            dates="2019.09.22",
            circles=[],
            media=media_,
            sources=[
                Source(
                    "Date, Participating circles: https://web.archive.org/web/20251107154156/http://yougakudan.blogspot.com/2016/10/blog-post_24.html",
                    (ReliabilityTypes.Reliable, OriginTypes.Official),
                ),
            ],
            locations=locations,
            description=None,
            # comments=None,
            last_edited="2026.10.18",
        )

        # Retrieve circles
        event.circles = retrieve_circles(event_name)
        events.append(event)

    i = 4  # ==== gensou_ningyou_sai4 ====
    if i not in disabled_events:
        event_name = f"gensou_ningyou_sai{i}"
        print(f"Processing {event_name} ...")

        media_ = [
            # Medium("", [Source("", (RT.Reliable, OT.Official))]),
            # Medium("", [Source("", (RT.Reliable, OT.Official))]),
            # Medium("", [Source("", (RT.Reliable, OT.Official))]),
        ]
        locations = [
            Location(
                coordinates=(35.5352689, 139.6991018),
                address="66-20 Horikawacho, Saiwai Ward, Kawasaki, Kanagawa 212-0013, Japan",
                description="川崎市産業振興会館",
                sources=[
                    Source(
                        "https://web.archive.org/web/20200202101652/http://yougakudann.dojin.com/index.html",
                        (ReliabilityTypes.Reliable, OriginTypes.OfficialExt),
                    )
                ],
                # comments=None,
                imageUrl="https://lh3.googleusercontent.com/gps-cs-s/AHRPTWnWztJ2ppoe3w-RXwZKQrT3vkgEbIN62FGlT7NE7zuGU7eM3ofV9HW_XPJIhG_gdXsqJye8REtNEDXEuXtA4hNE6eBFPNp2sgCSTD6dXYj3of4yaxjAaBFGG8WNY2Pr-rM431y9Sf2f9Zg=s0?imgmax=0",
                url="https://maps.app.goo.gl/GBVsEToTAegdTRpK8",
            ),
        ]
        event = Event(
            aliases=[
                "幻想人形祭4",
                "Gensou Ningyou Sai 4",
                "幻想人形祭(7th)",
                "Gensou Ningyou Sai (7th)",
            ],
            dates="2020.09.26",
            circles=[],
            media=media_,
            sources=[
                Source(
                    "Date: https://web.archive.org/web/20200202101652/http://yougakudann.dojin.com/index.html",
                    (ReliabilityTypes.Reliable, OriginTypes.Official),
                ),
                Source(
                    "Participating circles: https://x.com/yougakudan_info/status/1306931482003349505/photo/1",
                    (ReliabilityTypes.Reliable, OriginTypes.Official),
                ),
                Source(
                    "Participating circles (alt): https://web.archive.org/web/20200918213738/http://yougakudann.dojin.com/splist.html",
                    (ReliabilityTypes.Reliable, OriginTypes.Official),
                ),
                Source(
                    "NOT cancelled: https://x.com/yougakudan_info/status/1309738651878735873",
                    (ReliabilityTypes.Reliable, OriginTypes.Official),
                ),
            ],
            locations=locations,
            description="Simultaneous to 幺樂団カァニバル！10.",
            # comments=None,
            last_edited="2026.10.18",
        )

        # Retrieve circles
        event.circles = retrieve_circles(event_name)
        events.append(event)

    i = "4R"  # ==== gensou_ningyou_sai4R ====
    if i not in disabled_events:
        event_name = f"gensou_ningyou_sai{i}"
        print(f"Processing {event_name} ...")

        media_ = [
            # Medium("", [Source("", (RT.Reliable, OT.Official))]),
            # Medium("", [Source("", (RT.Reliable, OT.Official))]),
            # Medium("", [Source("", (RT.Reliable, OT.Official))]),
        ]
        locations = [
            Location(
                coordinates=(35.5352689, 139.6991018),
                address="66-20 Horikawacho, Saiwai Ward, Kawasaki, Kanagawa 212-0013, Japan",
                description="川崎市産業振興会館",
                sources=[
                    Source(
                        "https://web.archive.org/web/20210514014026/http://yougakudann.dojin.com/index.html",
                        (ReliabilityTypes.Reliable, OriginTypes.OfficialExt),
                    )
                ],
                # comments=None,
                imageUrl="https://lh3.googleusercontent.com/gps-cs-s/AHRPTWnWztJ2ppoe3w-RXwZKQrT3vkgEbIN62FGlT7NE7zuGU7eM3ofV9HW_XPJIhG_gdXsqJye8REtNEDXEuXtA4hNE6eBFPNp2sgCSTD6dXYj3of4yaxjAaBFGG8WNY2Pr-rM431y9Sf2f9Zg=s0?imgmax=0",
                url="https://maps.app.goo.gl/GBVsEToTAegdTRpK8",
            ),
        ]
        event = Event(
            aliases=[
                "幻想人形祭4R",
                "Gensou Ningyou Sai 4R",
                "幻想人形祭(8th)",
                "Gensou Ningyou Sai (8th)",
            ],
            dates="2021.02.27 → CANCELLED",
            circles=[],
            media=media_,
            sources=[
                Source(
                    "Date: https://web.archive.org/web/20210514014026/http://yougakudann.dojin.com/index.html",
                    (ReliabilityTypes.Reliable, OriginTypes.Official),
                ),
                # Source("Participating circles: ", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                Source(
                    "Cancelled: https://x.com/yougakudan_info/status/1354041811749097474",
                    (ReliabilityTypes.Reliable, OriginTypes.Official),
                ),
            ],
            locations=locations,
            description="Simultaneous to 幺樂団カァニバル！10R.",
            # comments=None,
            last_edited="2026.10.18",
        )

        # Retrieve circles
        # event.circles = retrieve_circles(event_name)
        events.append(event)

    i = 5  # ==== gensou_ningyou_sai5 ====
    if i not in disabled_events:
        event_name = f"gensou_ningyou_sai{i}"
        print(f"Processing {event_name} ...")

        media_ = [
            # Medium("", [Source("", (RT.Reliable, OT.Official))]),
            # Medium("", [Source("", (RT.Reliable, OT.Official))]),
            # Medium("", [Source("", (RT.Reliable, OT.Official))]),
        ]
        locations = [
            Location(
                coordinates=(35.655153, 139.7607689),
                address="Japan, 〒105-7501 Tokyo, Minato City, Kaigan, 1 Chome−7−1 東京ポートシティ竹芝オフィスタワ",
                comments=None,
                description="東京都立産業貿易センター 浜松町館",
                sources=[
                    Source(
                        "Official poster, see media.",
                        (RT.Reliable, OT.Official),
                    ),
                ],
                imageUrl="https://lh3.googleusercontent.com/gps-cs-s/AHRPTWmihIGbPitN7h8Vc_sXo8I679FTgrlkYst2LWaAy_Wl45MDqMaFnozSO4Y2Vud8h07FgRpXdq_CPW3IWnFwj-AyKuJ0L7ShZyQ41TQcBAFNOouYZR3jFZXxn_SQsgsK-FST-5JK8g=w408-h544-k-no",
                url="https://maps.app.goo.gl/ZF8XaGQinUTwnNMw6",
            ),
        ]
        event = Event(
            aliases=[
                "幻想人形祭5",
                "Gensou Ningyou Sai 5",
                "幻想人形祭(9th)",
                "Gensou Ningyou Sai (9th)",
            ],
            dates="2022.03.27",
            circles=[],
            media=media_,
            sources=[
                Source(
                    "Date, Participating circles: https://web.archive.org/web/20220307155313/http://yougakudann.dojin.com/splist.html",
                    (ReliabilityTypes.Reliable, OriginTypes.Official),
                ),
            ],
            locations=locations,
            description="Simultaneous to 幺樂団カァニバル！11.",
            # comments=None,
            last_edited="2026.10.18",
        )

        # Retrieve circles
        event.circles = retrieve_circles(event_name)
        events.append(event)

    i = 6  # ==== gensou_ningyou_sai6 ====
    if i not in disabled_events:
        event_name = f"gensou_ningyou_sai{i}"
        print(f"Processing {event_name} ...")

        media_ = [
            Medium(
                "06_531px-幻想人形祭9.jpg",
                [Source(thwikicc, (ReliabilityTypes.Likely, OriginTypes.External))],
            ),
            # Medium("", [Source("", (RT.Reliable, OT.Official))]),
            # Medium("", [Source("", (RT.Reliable, OT.Official))]),
        ]
        locations = [
            Location(
                coordinates=(35.655153, 139.7607689),
                address="Japan, 〒105-7501 Tokyo, Minato City, Kaigan, 1 Chome−7−1 東京ポートシティ竹芝オフィスタワ",
                comments=None,
                description="京都立産業貿易センター浜松町館　3階展示室南側",
                sources=[
                    Source(
                        "https://x.com/yougakudan_info/status/1677296406711910400",
                        (ReliabilityTypes.Reliable, OriginTypes.OfficialExt),
                    )
                ],
                imageUrl="https://lh3.googleusercontent.com/gps-cs-s/AHRPTWmihIGbPitN7h8Vc_sXo8I679FTgrlkYst2LWaAy_Wl45MDqMaFnozSO4Y2Vud8h07FgRpXdq_CPW3IWnFwj-AyKuJ0L7ShZyQ41TQcBAFNOouYZR3jFZXxn_SQsgsK-FST-5JK8g=w408-h544-k-no",
                url="https://maps.app.goo.gl/ZF8XaGQinUTwnNMw6",
            ),
        ]
        event = Event(
            aliases=[
                "幻想人形祭6",
                "Gensou Ningyou Sai 6",
                "幻想人形祭(10th)",
                "Gensou Ningyou Sai (10th)",
            ],
            dates="2023.07.09",
            circles=[],
            media=media_,
            sources=[
                Source(
                    "Date: https://x.com/yougakudan_info/status/1677296406711910400",
                    (ReliabilityTypes.Reliable, OriginTypes.Official),
                ),
                Source(
                    "Participating circles: https://web.archive.org/web/20240126080406/https://yougakudann.dojin.com/splist.html",
                    (ReliabilityTypes.Reliable, OriginTypes.Official),
                ),
            ],
            locations=locations,
            description="Simultaneous to 幺樂団カァニバル！12.",
            # comments=None,
            last_edited="2026.10.18",
        )

        # Retrieve circles
        event.circles = retrieve_circles(event_name)
        events.append(event)

    # i =   # ==== gensou_ningyou_sai ====
    # if i not in disabled_events:
    #     event_name = f"gensou_ningyou_sai{i}"
    #     print(f"Processing {event_name} ...")

    #     media_ = [
    #         # Medium("", [Source("", (RT.Reliable, OT.Official))]),
    #         # Medium("", [Source("", (RT.Reliable, OT.Official))]),
    #         # Medium("", [Source("", (RT.Reliable, OT.Official))]),
    #     ]
    #     locations = [
    #         # Location(
    #         #     coordinates=(,),
    #         #     address="",
    #         #     description="",
    #         #     sources=[Source("", (ReliabilityTypes.Reliable, OriginTypes.Official))],
    #         #     # comments=None,
    #         #     imageUrl="",
    #         #     url="",
    #         # ),
    #     ]
    #     event = Event(
    #         aliases=,
    #         dates="",
    #         circles=[],
    #         media=media_,
    #         sources=[
    #             # Source("Date: ", (RT.Reliable, OT.Official)),
    #             # Source("Participating circles: ", (RT.Reliable, OT.Official)),
    #         ],
    #         locations=locations,
    #         description=None,
    #         # comments=None,
    #         last_edited="2026.10.18",
    #     )

    #     # Retrieve circles
    #     # event.circles = retrieve_circles(event_name)
    #     events.append(event)

    # ==== event group ====
    media = [
        # Medium("",
        #        [Source("", (RT.Reliable, OT.Official))]),
        # Medium("",
        #        [Source("", (RT.Reliable, OT.Official))]),
    ]

    links = [
        "https://yougakudann.dojin.com/",
        "https://yougakudan.blogspot.com",
        "https://x.com/yougakudan_info",
        "https://x.com/yougakudann",
    ]

    event_group = EventGroup(
        aliases=[
            "幻想人形祭",
            "Gensou Ningyou Sai",
        ],
        events=events,
        media=media,
        links=links,
        sources=[
            # Source(
            #     "",
            #     (ReliabilityTypes.Reliable, OriginTypes.Official),
            # ),
        ],
        comments=None,
        description="Child doujin events of 幺樂団カァニバル！ (Yougakudann Carnival).",
        last_edited="2026.10.18",
    )

    print(f"Saving {Path(__file__).stem} database...")
    event_group.save(PATH_EVENT_GROUP, indent=None)
    print("Done")
